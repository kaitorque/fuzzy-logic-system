from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from fuzzy_project.helpers import *
from collections import namedtuple
from django.db import connection

now = timezone.now()
cursor = connection.cursor()
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
    page = { "title": "resources", "sub": "clientform" }
    if request.method == 'GET':
        return render(request, 'fuzzy_web/client_form.html', { "currentTime": now, "page": page })
    elif request.method == 'POST':
        #Declare array of errorMsg
        errorMsg = []
        #Custom Validation
        Input = namedtuple('Input',['name','value'])
        fullname = request.POST['fullname']
        age = request.POST['age']
        gender = request.POST['gender']
        cognitive = request.POST['cognitive']
        social = request.POST['social']
        emotional = request.POST['emotional']
        spiritual = request.POST['spiritual']
        physical = request.POST['physical']
        inputlist = [
            Input("Fullname", fullname),
            Input("Age", age),
            Input("Gender", gender),
            Input("Cognitive", cognitive),
            Input("Social", social),
            Input("Emotional", emotional),
            Input("Spiritual", spiritual),
            Input("Physical", physical)
        ]
        errorMsg.extend(checkEmpty(inputlist))
        inputlist = [
            Input("Age", age),
            Input("Cognitive", cognitive),
            Input("Social", social),
            Input("Emotional", emotional),
            Input("Spiritual", spiritual),
            Input("Physical", physical)
        ]
        errorMsg.extend(checkDigit(inputlist))
        if int(request.POST['age']) < 0:
            errorMsg.append("Age cannot less than 0")

        if not errorMsg:
            cursor.execute("INSERT INTO client "
            "(fullname, age, gender, cognitive, social, emotional, spiritual, physical)"
            " VALUES "
            "(%s, %s, %s, %s, %s, %s, %s, %s)", [fullname, int(age), gender, int(cognitive), int(social), int(emotional), int(spiritual), int(physical)])
            return JsonResponse({"success": True, "response": "Client successfully added!"})



        return JsonResponse({"success": False, "response": errorMsg})

def view_report(request):
    page = { "title": "resources", "sub": "client_form" }
    return render(request, 'fuzzy_web/view_report.html', { "currentTime": now, "page": page })
