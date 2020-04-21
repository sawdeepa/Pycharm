from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hi(request):
    return render(request,'Demochatapp/hi.html')
    #return HttpResponse('<h1>THIS IS MY HOME PAGE</h1>')
