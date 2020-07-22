from elasticsearch import Elasticsearch

from gui.Error import Error


class EsClient(object):

    def __init__(self):
        self.hostname = ''
        self.es = None
        self.version = '1'
        self.total = 0
        pass

    def open(self, ip, port):
        self.hostname = ip + ':' + str(port)
        self.es = Elasticsearch([{'host': ip, 'port': port}])


    def openHost(self, host):
        self.hostname = host
        strs = host.split(':')
        self.es = Elasticsearch([{'host': strs[0], 'port': strs[1]}])

    def testHost(self, host):
        self.openHost(host)
        print(self.es.info())

    def indices(self):
        indices = self.es.indices.get_alias()
        return indices.keys()

    def scheme(self, index):
        index_desc = self.es.indices.get(index)
        result = index_desc[index]['mappings']
        if 'properties' in result:
            return result
        else:
            for m in result:
                return result[m]

    def getHost(self):
        return self.hostname

    def getFieldName(self, index):
        doc = self.es.indices.get(index)
        modules = doc[index]['mappings']
        for m in modules:
            module = modules[m]
            for f in module['properties']:
                print(f, ' : ', module['properties'][f]['type'])
        return doc

    def getFieldNames(self, properties):
        result = []
        for f in properties:
            result.append(f)
            if f['type'] == 'nested':
                nested_list = self.getFieldNames(f['type']['properties'])
                for n in nested_list:
                    result.append(f + '.' + n)
        return result

    def search(self, index, query, page, size):
        self.build_page_query(page, query, size)
        print(query)

        queryData = self.es.search(
            index=index,
            body=query)

        self.total = queryData['hits']['total']
        if isinstance(self.total, dict):      # ES 5.7版本变更
            self.total = self.total['value']
        result = []
        for item in queryData['hits']['hits']:
            result.append(item['_source'])
        return result

    def build_page_query(self, page, query, size):
        query['from'] = (page - 1) * size
        if query['from'] > 10000:
            query['from'] = 10000 - size
        query['size'] = size

    def ignoreNone(self, doc):
        if isinstance(doc, list):
            result = []
            for item in doc:
                result.append(self.ignoreNone(item))
            return result
        elif isinstance(doc, dict):
            doc = self.removeEmpty(doc)
            return doc

    def removeEmpty(self, data):
        data2 = {}
        for o in data:
            if not data[o] is None:
                data2[o] = data[o]
        return data2
