from itertools import cycle

from streamparse import Spout


from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select
import json
import time

MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'root'
DB_NAME = 'storm'

metadata = MetaData()

# dialect+driver://username:password@host:port/database
engine = create_engine('mysql+pymysql://root:root@localhost:3306/storm')
connection = engine.connect()

#print(engine.table_names())
products = Table('products', metadata, autoload=True, autoload_with=engine)

# Show Columns details
# print(repr(products))


class ProductSpout(Spout):
    outputs = ['product']

    def initialize(self, stormconf, context, last_pid = 0):

        self.stormconf = stormconf
        self.context = context
        # self.last_pid = 0
        self.stmt = select([products]).limit(5).where(products.c.id > last_pid)
        self.result_obj =  connection.execute(self.stmt)
        self.products = iter([json.dumps(dict(row.items())) for row in self.result_obj ])

    def next_tuple(self):
        
        try:
            product = next(self.products)
            self.last_pid = eval(product).get('id', 0)
            time.sleep(5)

        except StopIteration as err:
            time.sleep(5)
            self.initialize(self.stormconf, self.context, last_pid=self.last_pid )

        else:
            self.emit([product])
            
        finally:
            pass
            



    
