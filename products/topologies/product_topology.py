"""
Word count topology
"""

from streamparse import Grouping, Topology

from spouts.products import ProductSpout
from spouts.user_profile_spout import UserProfileSpout
from bolts.product_save_bolt import ProductBolt


class WordCount(Topology):
    product_spout = ProductSpout.spec()
    user_profile_spout = UserProfileSpout.spec()

    product_bolt = ProductBolt.spec(inputs={product_spout: Grouping.fields('product')}, par=2)
    profile_bolt = ProductBolt.spec(inputs={user_profile_spout: Grouping.fields('profile')}, par=2)


