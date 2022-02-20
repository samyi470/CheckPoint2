from django.shortcuts import render
from django.http import HttpResponse


# hello world test
def index(request):
    return render(request, 'checkPointMng/home.html')
