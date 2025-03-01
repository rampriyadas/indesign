from django.shortcuts import render
from django.http import JsonResponse
#return JsonResponse(context)

def home(request):
   
    context ={}

    context["message"] = "Everything is Okay"
        
    return render(request, "home.html", context)

def addjob(request):
   
    context ={}

    context["message"] = "Everything is Okay"
        
    return render(request, "addjob.html", context)

def jobs(request):
   
    context ={}

    context["message"] = "Everything is Okay"
        
    return render(request, "jobs.html", context)