from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import os
import requests
import json
import pprint

os.environ['ALPHAVANTAGEAPIKEY'] = 'OR41UVDQX7XRVHBK'

url = "https://www.alphavantage.co/query"

function = "TIME_SERIES_DAILY"
symbol = "1301"
api_key = os.environ['ALPHAVANTAGEAPIKEY'];

data = { "function": function,
         "symbol": symbol,
         "apikey": api_key }
page = requests.get(url, params = data)
pprint.pprint(page.json())


ts = TimeSeries(key='OR41UVDQX7XRVHBK', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='TSLA',interval='60min', outputsize='full')
print data.plot()
plt.title('Intraday Times Series for TSLA stock (60 min)')
plt.show()
