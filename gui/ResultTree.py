from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem


class ResultTree(QTreeWidget):
    def __init__(self, parent=None):
        super(ResultTree, self).__init__(parent)
        self.properties = []
        self.isIgnoreNone = False
        self.setDragEnabled(True)

    def setIgnoreNone(self, ignoreNone):
        self.isIgnoreNone = ignoreNone
        pass

    def addTreeResult(self, result):
        self.clear()
        for doc in result:
            tree = QTreeWidgetItem(self)
            self.addTreeRecord(doc, tree)

    def addTreeRecord(self, doc, tree):
        if isinstance(doc, dict):
            tree.setText(0, "{doc}")
            tree.setText(1, '{ ' + str(len(doc.keys())) + ' fields }')
            tree.setText(2, 'Document')
            for field in doc:
                self.addTreeDict(field, doc[field], tree)

    def addTreeDict(self, field, doc, tree):
        if isinstance(doc, list):
            child = QTreeWidgetItem(tree)
            child.setText(0, field)
            child.setText(1, '[ ' + str(len(doc)) + ' elements ]')
            child.setText(2, self.getFieldType(field))
            for i, item in enumerate(doc):
                self.addTreeDict(str(i), item, child)
            return

        if isinstance(doc, dict):
            child = QTreeWidgetItem(tree)
            child.setText(0, field)
            child.setText(1, '{ ' + str(len(doc.keys())) + ' fields }')
            child.setText(2, self.getFieldType(field))
            for field in doc:
                self.addTreeDict(field, doc[field], child)
            return

        if doc is not None or self.isIgnoreNone:
            child = QTreeWidgetItem(tree)
            child.setText(0, field)
            child.setText(1, str(doc))
            child.setText(2, self.getFieldType(field))

    def getQuery(self, e):
        query = {}
        item = self.selectedItems()[0]
        path = self.get_path(item)

        query['field'] = path
        query['operator'] = 'match'
        query['value'] = item.text(1)
        return query

    def getFieldType(self, field):
        if field in self.properties:
            if 'properties' in self.properties[field]:
                return ''
            else:
                return self.properties[field]['type']
        else:
            return ''

    def get_path(self, item: QTreeWidgetItem):
        paths = []
        while item != None and item.text(0) != '{doc}':
            paths.insert(0, item.text(0))
            item = item.parent()
        return '.'.join(paths)
