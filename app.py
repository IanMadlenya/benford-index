from datetime import datetime
from pytz import timezone
import MySQLdb
import time
import database as database
import marketutil as util

# tickerlist includes: Shanghai Composite (000001.ss), S&P500 (%5EGSPC), FTSE100 (%5EFTSE), DAX (^gdaxi) and Nikkei225 (^n225)
# ticker (val 1) is the name that yahoo finance uses to describe the index while span (val 2) is the span on the page that the value sits in
tickerList={'000001.ss':'000001.ss','%5EGSPC':'^gspc','%5EFTSE':'^ftse','%5EGDAXI':'^gdaxi','%5EN225':'^n225'}

while True:
	for ticker,span in tickerList.items():
		if (util.marketIsOpen(ticker)):
			price=util.getYahooIndexPrice(ticker,span)
			#print(ticker,price)
			database.storeIndexPrice(price,ticker)
 	time.sleep(60)