'''
Followed instructions laid out by William Koehresen in the following two articles:
# https://towardsdatascience.com/stock-analysis-in-python-a0054e2c1a4c
# https://towardsdatascience.com/stock-prediction-in-python-b66555171a2
run file with command pythonw runStocker.py
'''
from stocker import Stocker

tesla = Stocker('TSLA')
print(tesla);
tesla.plot_stock(start_date=None, end_date=None, stats=['Adj. Close'], plot_type='basic')
tesla.predict_future(days=30)
