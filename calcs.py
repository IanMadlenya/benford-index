import numpy as np
benford=[30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6]

def getChiSquared(test,expected):
	chi_sq=0
	for t,e in zip(test,expected):
		print('testing :',t)
		print('expected: ',e)
		chi_sq=chi_sq+ ((t-e)*(t-e))/e
	return chi_sq

def passFailChi(chi):
	# degrees of freedom always 8 and assuming 95% confidence
	# from: https://en.wikipedia.org/wiki/Chi-squared_distribution
	# 95% conf: 15.51

	# Null hypothesis H_0: The first digits in the index minute price changes follow the Benford's law
	# Hypothesis H_1: The first digits in the index minute price changes do not follow the Benford's law}
	if (chi>15.51):
		return True
	else:
		return False

def getBenfordCount(data):
	#set initial dist to zero
	counts=[0,0,0,0,0,0,0,0,0]
	# for each figure, check what the first non-zero digit is, hacky multiply by 1000000 to handle small values
	for d in data:
		# sneaky multiply by 1000000 to ensure that the leading digit is unlikely to be zero
		# since benfords law is assumed to relate somehow to scale invariance, this *SHOULDN'T* make a difference
		# but it might, so this might all be wrong :-)
		s=str(np.abs(d)*1000000)
		for i in range(0,8):
			if(s.startswith(str(i+1))):
				counts[i]=counts[i]+1
				break
	return counts

def getExpectedBenfordCount(data):
	#set initial dist to zero
	size=len(data)
	expected_benford_counts=[]
	for b in benford:
		expected_benford_counts.append(b*0.01*size)
	return expected_benford_counts


def getBenfordDist(data):
	#set initial dist to zero
	dist=[0,0,0,0,0,0,0,0,0]
	# for each figure, check what the first non-zero digit is, hacky multiply by 1000000 to handle small values
	for d in data:
		# sneaky multiply by 1000000 to ensure that the leading digit is unlikely to be zero
		# since benfords law is assumed to relate somehow to scale invariance, this *SHOULDN'T* make a difference
		# but it might, so this might all be wrong :-)
		s=str(np.abs(d)*1000000)
		for i in range(0,8):
			if(s.startswith(str(i+1))):
				dist[i]=dist[i]+1
				break
	#return fractions of the total for each digit
	percentDist = []
	#convert to % - todo, start using numpy vectors that allow scalar mult/div
	for count in dist:
		percentDist.append(float(count)/len(data))
	return percentDist

def getBenfordDeviation(data):
	benford=[30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6]
	dev=[]
	for d in data:
		tempList=[]
		for i in range(0,9):
			tempList.append(float(benford[i])-float(d[i]))
		dev.append(tempList)
		return dev

def getPriceStepDifferences(data):
	differences=[]
	for i in range(0,len(data)-1):

		differences.append(np.abs(float(data[i+1])-float(data[i])))
	return differences

def getDayChangePercentage(data):
	return ((data[len(data)-1]-data[0])/data[0])