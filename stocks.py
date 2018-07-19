class StockRecord(object):

	def __init__(self, symbol):
		self.symbol = symbol
		self.recordNum = 0
		self.average = 0
		self.stocks = []

	def __str__(self):
		return('Symbol = {0}, Number of Records = {1}, Average = {2}'.format(self.symbol, self.recordNum, self.average))

	def updateRecordNum(self):
		self.recordNum =  len(self.stocks)

	def addStock(self, stock):
		self.stocks.append(stock)
		self.updateRecordNum()
		self.calculateAvg()

	def calculateAvg(self):
		runningTotal = 0;
		for stock in self.stocks:
			average  = stock.open + stock.close
			runningTotal += average
		self.average = runningTotal/(2*self.recordNum)

	def showRecords(self):
		for stock in self.stocks:
			print(stock)

class Stock(object):

	def __init__(self, id, open, close, high, low, volume):
			self.id = float(id)
			self.open =  float(open)
			self.close = float(close)
			self.high = float(high)
			self.low = float(low)
			self.volume = float(volume)

	def __str__(self):
		return('Id = {0}, Open Price = {1}, Close Price = {2}, High = {3}, Low = {4}, Volume = {5}'.format(self.id, self.open, self.close, self.high, self.low, self.volume))