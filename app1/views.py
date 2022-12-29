from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sujitha(request):
    return HttpResponse('<h1>Sujitha is my best friend</h1>')

def meena(request):
    return HttpResponse('<h2>Meena is my sister</h2>')