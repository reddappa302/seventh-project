from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def str1(request):
    return HttpResponse('this is firsts str response of APP1')

def str2(request):
    return HttpResponse('this is the secind str response of app1')    

