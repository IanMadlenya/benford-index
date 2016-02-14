from bs4 import BeautifulSoup
import parsers as parser
import database as database
import requests
import time
import MySQLdb
from dateutil import tz

# setup the database
db = MySQLdb.connect(host="localhost", 
                     user="benford",  
                     passwd="index", 
                     db="benfordindex")   
cur=db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS `data` (`id` int(255) NOT NULL primary key AUTO_INCREMENT, `timestamp` datetime NOT NULL, `price` decimal(8,2) NOT NULL, `ticker` varchar(32) NOT NULL)")
db.commit()

# function to grab index prices from yahoo finance using beautiful soup
def getYahooIndexPrice(ticker,spanID):
	r=requests.get("http://finance.yahoo.com/q?s="+ticker)
	data=r.text
	soup=BeautifulSoup(data,"lxml")
	price = soup.find('span', {'id': 'yfs_l10_'+spanID}).text.replace(',', '')
	return price

# function that works out if the market is open and stores the data if it is
# https://en.wikipedia.org/wiki/List_of_stock_exchange_opening_times
def marketIsOpen(ticker):
	#shanghai 09:15 to 15:00 
	if (ticker='000001.ss'):

	#new york 09:30 to 16:00 EST
	elif (ticker='%5EGSPC'):

	#london
	elif (ticker='%5EFTSE'):


	#frankfurt
	elif (ticker='^ftse'):

	#tokyo
	elif(ticker='^n225'):


	return True

# calculates the minute to minute differences of the index prices to generate a dataset o
def calculateMinutePriceDifferences(prices):


# returns a list of the leading digits of each price difference
def getLeadingDigits(priceDifferences):


def 	



# tickerlist includes: Shanghai Composite (000001.ss), S&P500 (%5EGSPC), FTSE100 (%5EFTSE), DAX (^gdaxi) and Nikkei225 (^n225)
tickerList={'000001.ss':'000001.ss','%5EGSPC':'^gspc','%5EFTSE':'^ftse','%5EGDAXI':'^gdaxi','%5EN225':'^n225'}

while True:
	for ticker,span in tickerList.items():
		localTZ = tz.tzlocal()
		now = datetime.utcnow()
		if (marketIsOpen(ticker)):
			price=getYahooIndexPrice(tick,span)
			print(tick,price)
			cur.execute('INSERT INTO data (timestamp,price,ticker) VALUES (%s,%s,%s)', (time.strftime('%Y-%m-%d %H:%M:%S'),price,ticker))
	 		db.commit()
 	time.sleep(60)