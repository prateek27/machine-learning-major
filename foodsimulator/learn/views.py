from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def save_data(request):
	if(request.method=="GET"):
		return HttpResponse("You made a GET Request!")
	else:	
		school_id=request.POST.get('school_id')
		school_total = request.POST.get('total_strenth')
		school_sent = request.POST.get('total_sent')
		school_left = request.POST.get('total_left')
		feedback = request.POST.get('feedback')

	print(feedback)
	print(school_left)