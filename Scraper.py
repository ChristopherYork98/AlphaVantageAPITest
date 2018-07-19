from timeseries import TimeSeries
import csv
from stocks  import StockRecord, Stock

myAPIkey = 'Your API KEY'

ts = TimeSeries(key=myAPIkey, output_format='csv', indexing_type='integer')

data, metadata = ts.get_intraday(symbol='ASX', interval='60min', outputsize='full')

IND = StockRecord(symbol='IND')

counter = 0
for row in data:
	if counter != 0:
			newStockEntry = Stock(counter, row[1], row[4], row[2], row[3], row[5])
			IND.addStock(newStockEntry)
	counter+=1

print(IND)
IND.showRecords()
print(IND)