from django.shortcuts import render

# Create your views here.
def firsttemplate(request):
    return render(request,'firsttemplate.html')

def second(request):
    return render(request,'second.html')    
