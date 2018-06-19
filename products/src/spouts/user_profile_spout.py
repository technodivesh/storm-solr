from streamparse import Spout
import requests
import time 
import simplejson

api_url = "http://localhost:5000/api/v1/profiles"

class UserProfileSpout(Spout):
    outputs = ['profile']

    def initialize(self, stormconf, context):
        self.stormconf = stormconf

        self.context = context
        # self.last_pid = 0


    def next_tuple(self):

        result = requests.get(api_url)
        # self.logger.info(result.json())
        self.emit([result.text])

        time.sleep(10)
        
        # try:
        #     product = next(self.products)
        #     self.last_pid = eval(product).get('id', 0)

        # except StopIteration as err:
        #     time.sleep(10)
        #     self.initialize(self.stormconf, self.context, last_pid=self.last_pid )

        # else:
        #     self.emit([product])
            
        # finally:
        #     pass