from random import randint

import os

test = []
def train():
		
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
				
			sc = school.objects.all()[0]

			od = order(school=sc,students_total=70,students_present=attendance,units_delivered=avg,units_left=avg-attendance,feedback="Decent")
			od.save()
		

		return test




if __name__ == '__main__':

	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodsimulator.settings')
	from learn.models import *	
	train()