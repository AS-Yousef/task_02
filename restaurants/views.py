from django.shortcuts import render
from django.http import HttpResponse

def restaurant(request):
	context={
	"msg":"Hello World!",
	}
	return render (request, 'resturant.html', context)
