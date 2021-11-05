import pandas as pd

from pandas_datareader import data

startDate = '2000-1-1'
endDate = '2020-12-31'
companies = ['VOO', 'MSFT', 'AAPL', 'AMZN', 'GOOGL','NVDA', 'JNJ', 'DIS', 'BIIB', 'SYY', 'PPG', 'GIS', 'YUM', 'KHC', 'WHR', 'PKG', 'PTC', 'HD', 'MRO']





# Adjusted close price
dfPrice = pd.DataFrame()

for ticker in companies:
	counter = 0
	print(ticker)
	dfPrice.insert(counter, ticker, data.DataReader(ticker, start=startDate, end=endDate, data_source='yahoo')['Adj Close'])
	counter += 1



dfPrice.to_excel("price.xlsx") 



#Current Metrics
dfMetrics = pd.DataFrame()

metrics= ['marketCap', 'sharesOutstanding', 'trailingPE', 'forwardPE', 'priceToBook', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'averageDailyVolume3Month']

for metric in metrics:
	counter = 0
	print(metric)
	dfMetrics.insert(counter, metric, data.get_quote_yahoo(companies)[metric])
	counter += 1


dfMetrics.to_excel("metrics.xlsx") 
