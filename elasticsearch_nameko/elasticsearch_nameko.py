import os
from datetime import datetime

from backoff_retry.retry import Retry

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import TransportError
from elasticsearch.helpers import bulk
from nameko.extensions import DependencyProvider
from nameko import config

from uuid import uuid4

retry = Retry(TransportError)

class ElasticSearchWrapper:

    def __init__(self, elasticsearch, index):

        self.elasticsearch = elasticsearch
        self.index = index

    @retry.backoff_strategy()
    def bulk_post(self, bulk_body):

        # Atualiza timestamp
        [x.update({'timestamp': datetime.utcnow()}) for x in bulk_body]

        # Atualiza o run id
        run_id = uuid4()        
        [x.update({'run_id': str(run_id)}) for x in bulk_body]

        # envia para o elasticsearch
        return bulk(self.elasticsearch, bulk_body, stats_only=True, index=self.index)


class ElasticSearch(DependencyProvider):

    @retry.backoff_strategy()
    def setup(self):

        self.elasticsearch = Elasticsearch()
        self.index = config.get('ELASTIC_INDEX')

        host = config.get('ELASTIC_HOST') 
        port = config.get('ELASTIC_PORT') 
        username = config.get('ELASTIC_USER') 
        password = config.get('ELASTIC_PASS')

        self.elasticsearch = Elasticsearch([f"{host}:{port}"],
                http_auth=(username, password),        
                sniff_on_start=True,
                sniff_on_connection_fail=True,
                sniffer_timeout=60)

    def get_dependency(self, worker_ctx):
        return ElasticSearchWrapper(self.elasticsearch, self.index)
