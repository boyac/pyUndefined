# return the max value of the High - Low stock price from the dataset (csv)
# Data from Quandl: https://www.quandl.com/data/XJPX/1319-Nomura-Asset-Management-Co-Ltd-1319-Adjusted-Stock-Prices
# 1319 | Nomura Nikkei 300 Listed ETF

with open('nomura_1319.csv', 'rb') as f:
	csv_reader = csv.reader(f)
	next(f) # call the next() to skip the header row
	mylist = []
	for i, row in enumerate(csv_reader):
		mylist.append((row[0], float(row[2]) - float(row[3])))
	
print max(mylist, key=(lambda x: x[1])) # ('2013-05-24', 34.955863233)
