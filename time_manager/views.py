from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import Employee,Hostname,StateChange

import json

def index(request):
	all_employees = Employee.objects.filter()
	context = {'employee_list': all_employees}
	return render(request, 'time_manager/index.html', context )

def detail(request, employee_id):
	employee = get_object_or_404(Employee, pk=employee_id)
	return render( request, "time_manager/detail.html", { 'employee':employee })

def time(request, employee_id):
	return HttpResponse("You're looking at time periods for employee %s." % employee_id )

@csrf_exempt
def stateupdate(request):
	if request.method == 'POST':
		data = request.POST
		data = data['data']
		all_employees = Employee.objects.all()
		all_hostnames = Hostname.objects.all()
		json_data = json.loads( data )

		for x in json_data:
				for h in all_hostnames:
					if x['hostname'] == h.string:
							lastStateChange = StateChange.objects.filter(employee_id=h.employee_id)
							if len(lastStateChange) > 0: #if blank (no records do else and add them)
								lastStateChange = StateChange.objects.filter(employee_id=h.employee_id).latest('state')
								if lastStateChange.state != x['active']: #if state changes, create a new object
									StateChange.objects.create(employee_id=h.employee_id,state=x['active'])
							else:
								StateChange.objects.create(employee_id=h.employee_id,state=x['active'])

		return HttpResponse(json_data)
	elif request.method == 'GET':
		return HttpResponse("Private Access Only")
