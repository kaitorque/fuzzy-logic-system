from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from fuzzy_project.helpers import *
from collections import namedtuple
from django.db import connection
from urllib.parse import parse_qs
from fuzzy_project.mamdani_calc import *

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
    cursor.execute("SELECT COUNT(id) as total, SUM(IF(gender = 'Male', 1, 0)) malecnt, SUM(IF(gender = 'Female', 1, 0)) femalecnt FROM client")
    datax = dictfetchone(cursor)
    datax['percentage'] = (datax['malecnt'] / datax['total']) * 100;
    return render(request, 'fuzzy_web/home.html', { "currentTime": now, "page": page, "data": datax })

def list_report(request):
    page = { "title": "resources", "sub": "listreport" }
    if request.method == 'GET':
        if 'step' in request.GET and request.GET['step'] == "clienttable":
            cursor.execute("SELECT * FROM client")
            datax = dictfetchall(cursor)
            datay = list(map(cLink , datax))
            return JsonResponse({"data": datay })
        else:
            return render(request, 'fuzzy_web/list_report.html', { "currentTime": now, "page": page })
    elif request.method == 'POST':
        #Declare array of errorMsg
        errorMsg = []
        if request.POST['step'] == "delete":
            delid = parse_qs(decrypt(request.POST['delid']))
            cursor.execute("DELETE FROM client WHERE id = %s", delid["id"])
            if cursor.rowcount > 0:
                response = "Client record successfully deleted!"
            else:
                response = "No change detected. No record updated!"
            return JsonResponse({"success": True, "response": response})
        else:
            errorMsg.append("Request Error")
        return JsonResponse({"success": False, "response": errorMsg})



def client_form(request):
    page = { "title": "resources", "sub": "clientform" }
    if request.method == 'GET':
        return render(request, 'fuzzy_web/client_form.html', { "currentTime": now, "page": page })
    elif request.method == 'POST':
        #Declare array of errorMsg
        errorMsg = []
        if request.POST['step'] == "add":
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
            #if no error
            if not errorMsg:
                cursor.execute("INSERT INTO client "
                "(fullname, age, gender, cognitive, social, emotional, spiritual, physical)"
                " VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s)", [fullname, int(age), gender, int(cognitive), int(social), int(emotional), int(spiritual), int(physical)])
                return JsonResponse({"success": True, "response": "Client successfully added!"})
        else:
            errorMsg.append("Request Error")
        return JsonResponse({"success": False, "response": errorMsg})

def view_report(request):
    page = { "title": "resources", "sub": "client_form" }
    if request.method == 'GET':
        delid = parse_qs(decrypt(request.GET['q']))
        cursor.execute("SELECT * FROM client WHERE id = %s", delid["id"])
        datax = dictfetchone(cursor)
        fuzzy_calc(datax)
        link = "cog/"+str(datax["id"])+".png"
        return render(request, 'fuzzy_web/view_report.html', { "currentTime": now, "page": page, "data": datax, "link": link })
    else:
        errorMsg = []
        errorMsg.append("Request Error")
        return JsonResponse({"success": False, "response": errorMsg})
