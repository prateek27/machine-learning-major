from sklearn import linear_model
from random import randint


def train():
	test = []
	sum = 0
	for i in range(0,500):
		test.append([])
	prev = 50
	for i in range(0,500):
		attendance = prev - randint(0,10) + randint(0,10)
		attendance = max(attendance,30)
		attendance = min(attendance,70)
		sum = sum + attendance
		avg = sum - attendance
		avg/= max(1,i)
		test[i].append(avg)
		test[i].append(prev)
		test[i].append(avg-attendance)
		prev = attendance
	return test

def generateX(testdata):
	X = []
	for i in range(len(testdata)):
		X.append([])
	for i in range(len(testdata)):
		X[i].append(testdata[i][0])	
		X[i].append(testdata[i][1])
	return X

def generateY(testdata):
	Y = []
	for i in range(len(testdata)):
		Y.append(testdata[i][2])
	return Y

def update(testdata,attendance):
	length = len(testdata)
	sum = length*testdata[length-1][0]
	sum = sum + attendance 
	avg = sum/(length+1)
	prev = testdata[length-1][0] - testdata[length-1][2]
	testdata.append([])
	testdata[length].append(avg)
	testdata[length].append(prev)
	testdata[length].append(avg-attendance)
	return testdata

def findNext(X,Y,testdata):
	clf = linear_model.LinearRegression()
	clf.fit(X,Y)
	length = len(testdata)
	sum = length*testdata[length-1][0]
	prev = testdata[length-1][1]
	avg = sum/length
	predicted_Attendance = avg - clf.intercept_ - avg*clf.coef_[0] - prev*clf.coef_[1]
	return int(predicted_Attendance)



def CompareError(X,Y,testdata):

	clf = linear_model.LinearRegression()
	clf.fit(X,Y)
	length = len(testdata)
	n = 100
	sum = testdata[length-1][0]*length
	errorInitially = 0
	errorAfterML = 0
	prev = testdata[length-1][1]
	for i in range(0,n):
		attendance = prev + randint(0,10) - randint(0,10)
		attendance = min(attendance,70)
		attendance = max(attendance,30)
		avg = sum
		avg/=(length+i)
		sum = sum + attendance
		predicted_Attendance = avg - clf.intercept_ - avg*clf.coef_[0] - prev*clf.coef_[1]
		errorInitially += abs(avg-attendance)
		errorAfterML += abs(predicted_Attendance-attendance)
		X.append([])
		X[length+i].append(avg)
		X[length+i].append(prev)
		Y.append(avg-attendance)
		prev = attendance
		clf.fit(X,Y)
		print(errorInitially/n)
		print(errorAfterML/n)

def main():

	testdata = []
	testdata = train()
	X = generateX(testdata)
	Y = generateY(testdata)
		

main()