import os
from collections import Counter
import simplejson

from streamparse import Bolt

# from SolrClient import SolrClient
# solr = SolrClient('http://localhost:8983/solr')

import requests 
url = 'http://localhost:8983/solr/products/update/json/docs?commit=true' 
header = {'Content-Type':'application/json'}


class ProductBolt(Bolt):
    outputs = ['product']

    def initialize(self, conf, ctx):
        self.counter = Counter()
        self.pid = os.getpid()
        self.total = 0

    def _increment(self, product, inc_by):
        self.counter[product] += inc_by
        self.total += inc_by

    def process(self, tup):

        # self.logger.info(tup)

        docs = tup.values[0]

        # To print the document
        self.logger.info(docs)
        # To index the document in apache solr
        # requests.post(url=url, data=docs, headers=header)

        # self.logger.info(res.status_code)        


        # self.logger.info(docs)
        # self.logger.info(type(docs))
        # docs =  [{"pkey": "M-263A-00003-003", "id": 19, "title": "Multi-Vitamin Juice TEST DIVESH 19 --", "site_id": 3, "job_id": 3},]
        # self.logger.info(docs)
        # solr.index_json('storm-stream', simplejson.dumps(docs))





        # product = tup.values[0]
        # self._increment(product, 10 if product == "dog" else 1)
        # if self.total % 1000 == 0:
        #     self.logger.info("counted [{:,}] products [pid={}]".format(self.total,
        #                                                             self.pid))
        # self.emit([product, self.counter[product]])