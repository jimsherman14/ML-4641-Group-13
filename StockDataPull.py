import pandas as pd

from pandas_datareader import data

startDate = '2000-1-1'
endDate = '2020-12-31'
companies = ['MSFT', 'AAPL', 'AMZN', 'GOOGL','NVDA', 'JNJ', 'DIS', 'BIIB', 'SYY', 'PPG', 'GIS', 'YUM', 'KHC', 'WHR', 'PKG', 'PTC', 'HD', 'MRO']

# Only get the adjusted close.
voo = data.DataReader("VOO", start=startDate, end=endDate, data_source='yahoo')['Adj Close']
df = pd.DataFrame(voo)

for ticker in companies:
	counter = 1
	print(ticker)
	df.insert(counter, ticker, data.DataReader(ticker, start=startDate, end=endDate, data_source='yahoo')['Adj Close'])
	counter += 1



df.to_excel("output.xlsx") 