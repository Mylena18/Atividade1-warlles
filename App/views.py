from django.shortcuts import render
from django.http import HttpResponse

def boas_vindas(request):
    return HttpResponse("Boas vindas")
# Create your views here.
