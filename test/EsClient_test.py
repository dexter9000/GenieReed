import unittest
from es.EsClient import EsClient


class EsClientTest(unittest.TestCase):

    def test_indices(self):
        """Test method add(a, b)"""
        client = EsClient()
        client.open('172.16.1.59', '9200')
        result = client.indices()
        print(result)

    def test_scheme(self):
        client = EsClient()
        client.open('172.16.1.59', '9200')
        result = client.scheme("cdp_elelc_customer")
        print(result)
        result = client.getFields("cdp_elelc_customer")

    def test_search(self):
        client = EsClient()
        client.open('172.16.1.59', '9200')

        index = 'cdp_bbelc_customer'
        query = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match_all": {}
                        }
                    ],
                    "must_not": [],
                    "should": []
                }
            },
            "_source":{
                "excludes":[
                    "cdp_field_weight"
                ]
            },
            "from": 0,
            "size": 10,
            "sort": [],
            "aggs": {}
        }
        page = 1
        size = 10
        result = client.search(index, query, page, size)

        result = client.ignoreNone(result)
        print(result)
        pass


if __name__ == '__main__':
    unittest.main()
