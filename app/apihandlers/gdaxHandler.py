#GDAX API Handler using GDAX's unofficial client package

#importing GDAX package from local directory
import sys
from app.apihandlers.classstructure import *

sys.path.insert(0,'C:/Users/Yong Zhen Yu/Documents/gdax-python/gdax')
sys.path.insert(0,'C:/Users/Yong Zhen Yu/Documents/gdax-python')

import gdax

class gdaxPublic(exchangeAPI)
	public_client = gdax.PublicClient()

	public_client.get_product_historic_rates("ETH-USD")

	def __init__(self):
		super(exchangeAPI, self).__init__()


