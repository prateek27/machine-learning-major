from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.

class school(models.Model):
	school_name = models.CharField(max_length=200)
	school_strength = models.IntegerField()
	school_deliveryBoy = models.ForeignKey(User)

	def __str__(self):
		return self.school_name 

		

class order(models.Model):
	date = models.DateTimeField(default = timezone.now())
	school = models.ForeignKey(school)

	students_present = models.IntegerField(default=0)
	students_total = models.IntegerField(default=0)

	units_delivered = models.IntegerField(default=0)
	units_left = models.IntegerField(default=0)
	feedback= models.CharField(max_length=200)

	def __str__(self):
		return str(self.school.school_name + str(self.units_delivered) + "/" + str(self.units_left)) 

class result(models.Model):
	students = models.IntegerField(default=45)
	lr = models.IntegerField(default=45)
	rr = models.IntegerField(default=45)
	svm = models.IntegerField(default=45)
	
	def __str__(self):
		return str(self.school.school_name + str(self.units_delivered) + "/" + str(self.units_left)) 