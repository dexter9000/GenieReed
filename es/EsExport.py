def export(es, index, query, outFile):
    page_size = 500
    query['size'] = page_size
    queryData = es.search(
        index=index,
        scroll='5m',
        body=query)

    # 1. 创建文件对象
    f = open(outFile, 'w', encoding='utf-8')

    for value in queryData['hits']['hits']:
        message = [value][0]['_source']['message']
        f.write(message + '\n')

    scroll_id = queryData["_scroll_id"]
    total = int(queryData["hits"]["total"])

    page_num = int(total / page_size) + 1

    # page_num = 1
    for i in range(page_num):
        res = es.scroll(scroll_id=scroll_id, scroll='5m')

        for value in res['hits']['hits']:
            message = [value][0]['_source']['message']
            f.write(message + '\n')

    f.close()
    pass
