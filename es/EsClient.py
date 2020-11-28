from elasticsearch import Elasticsearch


def build_page_query(query, page, size):
    if 'from' not in query:
        query['from'] = (page - 1) * size
        if query['from'] > 10000:
            query['from'] = 10000 - size
    if 'size' not in query:
        query['size'] = size


def removeEmpty(data):
    data2 = {}
    for o in data:
        if not data[o] is None:
            data2[o] = data[o]
    return data2


class EsClient(object):

    def __init__(self):
        self.hostname = ''
        self.username = ''
        self.password = ''
        self.es = None
        self.version = '1'
        self.total = 0
        pass

    def open(self, ip, port, username, password):
        self.hostname = ip + ':' + str(port)
        self.username = username
        self.password = password

        if not username or not password:
            self.es = Elasticsearch([{'host': ip, 'port': port}])
        else:
            self.es = Elasticsearch([{'host': ip, 'port': port, 'http_auth': (username, password)}])

    def openHost(self, host, username, password):
        self.hostname = host
        self.username = username
        self.password = password

        strs = host.split(':')
        if not username or not password:
            self.es = Elasticsearch([{'host': strs[0], 'port': strs[1]}])
        else:
            self.es = Elasticsearch([{'host': strs[0], 'port': strs[1], 'http_auth': (username, password)}])

    def testHost(self, host, username, password):
        self.openHost(host, username, password)
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

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

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
        build_page_query(query, page, size)
        print(query)

        queryData = self.es.search(
            index=index,
            body=query)

        self.total = queryData['hits']['total']
        if isinstance(self.total, dict):  # ES 5.7版本变更
            self.total = self.total['value']
        result = []
        for item in queryData['hits']['hits']:
            result.append(item['_source'])
        return result

    def ignoreNone(self, doc):
        if isinstance(doc, list):
            result = []
            for item in doc:
                result.append(self.ignoreNone(item))
            return result
        elif isinstance(doc, dict):
            doc = removeEmpty(doc)
            return doc
