from django.shortcuts import render
from cowin_api import CoWinAPI
from datetime import date
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method == "POST":
        pincode = request.POST["pin"]
        age = request.POST["age"]
        today = date.today()
        date_now = today.strftime("%d-%m-%Y")
        pin_code = pincode
        da = date_now
        min_age_limit = age
        cowin = CoWinAPI()
        index.available_centers = cowin.get_availability_by_pincode(pin_code, da, int(min_age_limit))
        return HttpResponseRedirect(reverse("results"))
    return render(request, "appointment/index.html")
    
def results(request):
    ans = []
    print(index.available_centers)
    for each in index.available_centers["centers"]:
        y = []
        y.append(each["address"])
        y.append(each["sessions"][0]["slots"])
        y.append(each["sessions"][0]["vaccine"])
        y.append(each["sessions"][0]["date"])
        y.append(each["sessions"][0]["available_capacity"])
        ans.append(y)
    print(ans)
    return render(request, "appointment/results.html", {
        "results": ans
    })
