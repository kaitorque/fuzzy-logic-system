from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

now = timezone.now()
# import datetime
#
# now = datetime.datetime.now()

# Create your views here.

def empty(request):
    page = { "title": "empty", "sub": "" }
    return render(request, 'fuzzy_web/empty.html', { "currentTime": now, "page": page })

def home(request):
    page = { "title": "home", "sub": "" }
    return render(request, 'fuzzy_web/home.html', { "currentTime": now, "page": page })

def list_report(request):
    page = { "title": "resources", "sub": "listreport" }
    return render(request, 'fuzzy_web/list_report.html', { "currentTime": now, "page": page })

def client_form(request):
    page = { "title": "resources", "sub": "client_form" }
    return render(request, 'fuzzy_web/client_form.html', { "currentTime": now, "page": page })

def view_report(request):
    page = { "title": "resources", "sub": "client_form" }
    return render(request, 'fuzzy_web/view_report.html', { "currentTime": now, "page": page })