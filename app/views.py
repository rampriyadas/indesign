from django.shortcuts import render
from django.http import JsonResponse
#return JsonResponse(context)

def home(request):
   
    context ={}

    context["message"] = "Everything is Okay"
        
    return render(request, "home.html", context)
    