from django.http import HttpResponse
from django.shortcuts import render 





def home(request):
    return render(request, "home.html", context={"name": "Arthur"})
 
 def testingithub(request):
    return HttpResponse("Testando o github")