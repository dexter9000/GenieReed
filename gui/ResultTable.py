from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class ResultTable(QTableWidget):
    def __init__(self, parent=None):
        super(ResultTable, self).__init__(parent)
        self.setDragEnabled(True)

    def addTableResult(self, result):
        fields = []
        for i in range(self.rowCount()):
            self.removeRow(0)

        if (isinstance(result, list)):
            if (len(result) <= 0):
                return
            fields = self.getFields(result[0])
        elif (isinstance(result, dict)):
            fields = self.getFields(result)

        self.setColumnCount(len(fields))
        self.setHorizontalHeaderLabels(fields)
        self.setRowCount(len(result))

        for rowNum, item in enumerate(result):
            self.addTableRow(rowNum, item, fields)

    def addTableRow(self, rowNum, line, fields):
        for colNum, field in enumerate(fields):
            if field in line:
                item = QTableWidgetItem(str(line[field]))
                item.setToolTip(str(line[field]))
                self.setItem(rowNum, colNum, item)

    def getFields(self, doc):
        result = []
        for f in doc:
            result.append(f)
        result = sorted(result, key=str.lower)
        return result

    def getQuery(self, e):
        query = {}
        item = self.selectedItems()[0]
        column = self.column(item)
        query['field'] = self.horizontalHeaderItem(column).text()
        query['operator'] = 'match'
        query['value'] = item.text()
        return query
