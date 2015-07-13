from django.db import models

# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class TimePeriod(models.Model):
	employee = models.ForeignKey(Employee)
	day = models.DateField('day')
	clock_in = models.DateTimeField('time in')
	clock_out= models.DateTimeField('time out')
	hours = models.IntegerField()
	overtime = models.IntegerField()
	def __str__(self):
		return self.day.strftime('%Y-%m-%d')

class StateChange(models.Model):
	employee_id = models.ForeignKey(Employee)
	state = models.BooleanField()
	time = models.DateTimeField(auto_now=True)
	def __str__(self):
		if self.state:
			return "Active: " + self.time.strftime('%c')
		else:
			return "Inactive: " + self.time.strftime('%c')

class Hostname(models.Model):
	employee_id = models.ForeignKey(Employee)
	string = models.CharField(max_length=200)
	active = models.BooleanField()
	def __str__(self):
		return self.string
