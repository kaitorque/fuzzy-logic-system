from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

now = timezone.now()
# import datetime
#
# now = datetime.datetime.now()

# Create your views here.

def hi(request):
    return render(request,'fuzzy_web/hi.html')

def index(request):
    return render(request, 'fuzzy_web/index.html')

def empty(request):
    return render(request, 'fuzzy_web/empty.html', { "currentTime": now })

def home(request):
    return render(request, 'fuzzy_web/home.html', { "currentTime": now })

def list_report(request):
    return render(request, 'fuzzy_web/list_report.html', { "currentTime": now })
