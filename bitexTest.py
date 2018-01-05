from bitex.interface import *
import time
import bitex
import requests

bfx = bitfinex.Bitfinex()
response = bfx.order_book('btcusd')
response.content
