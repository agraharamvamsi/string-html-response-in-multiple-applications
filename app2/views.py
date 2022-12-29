from django.shortcuts import render

# Create your views here.
def first(request):
    d={'python':'santhosh'}
    return render(request,'first.html',d)
def second(request):
    d={'django':'Harshadvali'}
    return render(request,'second.html',d)