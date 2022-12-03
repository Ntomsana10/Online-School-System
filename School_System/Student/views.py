from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Student_details(request):

    return HttpResponse('<h1>We Are Live<h1/>')
