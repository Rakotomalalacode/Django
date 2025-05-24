from django.shortcuts import render

# Create your views here.

def Hello (request , name) :
    return render(request , 'film/Hello.html' , {'params':name})