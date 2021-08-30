from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def latest_news(request):
    return HttpResponse('This is news!')
