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
fileName='testdata_sp500.csv'
## For now, let's just use test data

with open(fileName, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		minutePriceCloses.append(row[2])

# calculate the price changes from minute to minute		
minutePriceChanges=calc.getPriceStepDifferences(minutePriceCloses)
# calculate the percentage distribution of leading digits for these changes
benford_test_data_dist=calc.getBenfordDist(minutePriceChanges)
# count how many instances of each leading digit occur
benford_test_count=calc.getBenfordCount(minutePriceChanges)
# calculate how many you would have expected to occur if benfords law held
benford_exp_count=calc.getExpectedBenfordCount(minutePriceChanges)
#calculate the chi-sq value to estimate the probability that the results follow benfords law
chi_sq=calc.getChiSquared(benford_test_count,benford_exp_count)
print("Chi Sq: "+str(chi_sq))

#setup plotting
ind=np.arange(1,10)
width = 0.35
plt.figure(1)
plt.subplot(211)
plt.title(fileName)
plt.plot(minutePriceCloses)
plt.ylabel('Security Price')
plt.xlabel('Time Step (minutes)')

plt.subplot(212)
plt.xlabel('Leading Digit')
plt.ylabel('P(d)')
plt.xlim(0.5,10)
plt.xticks([1,2,3,4,5,6,7,8,9])

p1=plt.bar(ind,benford,width,color='b', align='center')
p2=plt.bar(ind+width,benford_test_data_dist,width, color='r', align='center')
plt.legend((p1[0],p2[0]),('Benfords Law','Test Data'))
plt.show()