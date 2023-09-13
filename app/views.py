from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_top(request):
    teo=TopicForm()
    d={'teo':teo}
    if request.method=='POST':
        tdo=TopicForm(request.POST)
        if tdo.is_valid():
            tdo.save()
            return HttpResponse('inserted')

    return render(request,'insert_top.html',d)

def insert_web(request):
    weo=WebpageForm()
    d={'weo':weo}
    if request.method=='POST':
        wdo=WebpageForm(request.POST)
        if wdo.is_valid():
            wdo.save()
            return HttpResponse('data inserted')

    return render(request,'insert_web.html',d)