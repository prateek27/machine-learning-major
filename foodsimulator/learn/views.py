from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from learn.models import school,order
from random import randint
from sklearn import linear_model

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at food simulator.")


@csrf_exempt
def save_data(request):
	
	if(request.method=="GET"):
		return render(request,"index.html")
	else:	
		print(request)

		#school_id = request.POST.get('school_id')
		total = request.GET.get('students_total')
		present = request.GET.get('students_present')
		
		utotal = request.GET.get('units_delivered')
		uleft = request.GET.get('units_left')
		
		feedback = request.GET.get('feedback')


		
		school_list = school.objects.all()
		first = school_list[0]
	
		print(first.school_name)
		print(total)
		print(present)
		print(utotal)
		print(uleft)

		od = order(school=first,students_present=int(present),students_total=int(total),units_delivered=int(utotal),units_left=int(uleft),feedback=feedback)
		od.save()	
		
		test_data = train()
		test_data = update(test_data,int(present))
		x = generateX(test_data)
		y = generateY(test_data)
		print("predicted value is "+str(findNext(x,y,test_data)))
		CompareError(x,y,test_data)
		return HttpResponse("Ok")



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

def findNext(X,Y,testdata):
	clf = linear_model.LinearRegression()
	clf.fit(X,Y)
	length = len(testdata)
	sum = length*testdata[length-1][0]
	prev = testdata[length-1][1]
	avg = sum/length
	predicted_Attendance = avg - clf.intercept_ - avg*clf.coef_[0] - prev*clf.coef_[1]
	return int(predicted_Attendance)

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