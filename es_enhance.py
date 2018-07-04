# coding: utf-8


from elasticsearch import Elasticsearch
import log


class es:
    def __init__(self, host, port):
        try:
            self.es = Elasticsearch([{'host': host, 'port': port}])
            self.def_body = {'query': {
                'query_string': {'analyze_wildcard': False, 'query': '*'}}}
        except Exception as e:
            log.record("[ERROR]es.__init__: %s" % str(e))
        pass

    def delete(self, index, doc_type, body):
        if body == None:
            body = self.def_body
        try:
            result = self.es.search(index=index, doc_type=doc_type, body=body)
        except Exception as e:
            log.record("[ERROR]es.search: %s" % str(e))
            return 1
        hits = result['hits']['hits']
        for hit in hits:
            try:
                self.es.delete(index=hit["_index"], doc_type=hit["_type"],
                               id=hit["_id"])
            except Exception as e:
                log.record("[ERROR]es.delete: %s" % str(e))
                return 2
        return 0
        pass

    def search(self, index, doc_type, body):
        if body == None:
            body = self.def_body
        try:
            result = self.es.search(index=index, doc_type=doc_type, body=body)
        except Exception as e:
            log.record("[ERROR]es.search: %s" % str(e))
            return None
        return result
        pass


if __name__ == "__main__":
    pass
