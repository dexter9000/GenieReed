from elasticsearch import Elasticsearch
import json


class EsClient(object):

    def __init__(self):
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
        return self.es.indices.get(index)[index]['mappings']

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
        return result

    def search(self, index, query, page, size):
        query['from'] = (page - 1) * size
        if query['from'] > 10000:
            query['from'] = 10000 - size
        query['size'] = size
        print(query)

        queryData = self.es.search(
            index=index,
            body=query)
        self.total = queryData['hits']['total']
        result = []
        for item in queryData['hits']['hits']:
            result.append(item['_source'])
        return result

    def ignoreNone(self, doc):
        if (isinstance(doc, list)):
            result = []
            for item in doc:
                result.append(self.ignoreNone(item))
            return result
        elif (isinstance(doc, dict)):
            doc = self.removeEmpty(doc)
            return doc

    def removeEmpty(self, data):
        data2 = {}
        for o in data:
            if not data[o] == None:
                data2[o] = data[o]
        return data2