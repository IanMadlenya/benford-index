import MySQLdb
import marketutil as util

# setup the database

db = MySQLdb.connect(host="localhost", 
                      user="benford",  
                      passwd="index", 
                      db="benfordindex")   
cur=db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS `data` (`id` int(255) NOT NULL primary key AUTO_INCREMENT, `timestamp` datetime NOT NULL, `price` decimal(8,2) NOT NULL, `ticker` varchar(32) NOT NULL)")
db.commit()

#generic database storage
def storeIndexPrice(price,ticker):
	cur=db.cursor()
	cur.execute('INSERT INTO data (timestamp,price,ticker) VALUES (%s,%s,%s)', (util.getLocalTime(ticker),price,util.getCleanTicker(ticker)))
	db.commit()
	return True

# generic database retrieval function
def retrievefromDatabase():
	return True

def getIndexDailyData(ticker,date):
	return True