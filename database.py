import MySQLdb
import marketutil as util
import datetime as dt

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

def getIndexDailyData(ticker,sy,sm,sd,ey,em,ed):
	cur=db.cursor()
	startDate=dt.date(sy,sm,sd)
	endDate=dt.date(ey,em,ed)
	cur.execute('SELECT * FROM data WHERE timestamp > %s AND timestamp <%s AND ticker LIKE %s ORDER BY `timestamp` ASC',(startDate,endDate,ticker))
	db.commit()
	data=cur.fetchall()
	if not cur.rowcount:
		print "No results found"
		print(cur._last_executed)
	else:
		for row in cur:
			print row[1],row[2]