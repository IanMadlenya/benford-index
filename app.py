from datetime import datetime
from pytz import timezone
import MySQLdb
import time
import database as database
import marketutil as util
import csv
import calcs as calc
import matplotlib.pyplot as plt
import numpy as np

# tickerlist includes: Shanghai Composite (000001.ss), S&P500 (%5EGSPC), FTSE100 (%5EFTSE), DAX (^gdaxi) and Nikkei225 (^n225)
# ticker (val 1) is the name that yahoo finance uses to describe the index while span (val 2) is the span on the page that the value sits in

####
# SCRAPER CODE to get index values from yahoo finance - commented out for demo
####


# tickerList={'000001.ss':'000001.ss','%5EGSPC':'^gspc','%5EFTSE':'^ftse','%5EGDAXI':'^gdaxi','%5EN225':'^n225'}

# while True:
# 	for ticker,span in tickerList.items():
# 		if (util.marketIsOpen(ticker)):
# 			try:
# 				price=util.getYahooIndexPrice(ticker,span)
# 				#print(ticker,price)
# 				database.storeIndexPrice(price,ticker)
# 			except:
# 				pass
#  	time.sleep(60)
benford=[0.301,0.176,0.125,0.097,0.079,0.067,0.058,0.051,0.046]
minutePriceCloses=[]
with open('testdata_sp500.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		minutePriceCloses.append(row[2])
minutePriceChanges=calc.getPriceStepDifferences(minutePriceCloses)

benford_test_data_dist=calc.getBenfordDist(minutePriceChanges)

benford_test_count=calc.getBenfordCount(minutePriceChanges)
print("actual counts: "+str(benford_test_count))
benford_exp_count=calc.getExpectedBenfordCount(minutePriceChanges)
print("expected counts: "+str(benford_exp_count))

chi_sq=calc.getChiSquared(benford_test_count,benford_exp_count)
print("Chi Sq: "+str(chi_sq))

ind=np.arange(9)
plt.figure(1)
plt.subplot(211)
width = 0.35
plt.plot(minutePriceCloses)
plt.subplot(212)
p1=plt.bar(ind,benford,width,color='b')
p2=plt.bar(ind+width,benford_test_data_dist,width, color='r')
plt.legend((p1[0],p2[0]),('Benfords Law','Test Data'))
plt.show()