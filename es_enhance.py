# coding: utf-8


from elasticsearch import Elasticsearch


class es:
    def __init__(self, host, port):
        try:
            self.es = Elasticsearch([{'host': host, 'port': port}])
            self.def_body = {'query': {
                'query_string': {'analyze_wildcard': False, 'query': '*'}}}
        except Exception as e:
            print("[ERROR]es.__init__: " + str(e))
        pass

    def delete(self, index, doc_type, body):
        if body == None:
            body = self.def_body
        try:
            result = self.es.search(index=index, doc_type=doc_type, body=body)
        except Exception as e:
            print("[ERROR]es.search: " + str(e))
            return 1
        hits = result['hits']['hits']
        for hit in hits:
            try:
                self.es.delete(index=hit["_index"], doc_type=hit["_type"],
                               id=hit["_id"])
            except Exception as e:
                print("[ERROR]es.delete: " + str(e))
                return 2
        return 0
        pass

    def search(self, index, doc_type, body):
        if body == None:
            body = self.def_body
        try:
            result = self.es.search(index=index, doc_type=doc_type, body=body)
        except Exception as e:
            print("[ERROR]es.search: " + str(e))
            return None
        total = len(result['hits']['hits'])
        hits_info = {}
        hits_info['total'] = total
        hits_info['hits'] = result['hits']['hits']
        return hits_info
        pass


if __name__ == "__main__":
    pass
