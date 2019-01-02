from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from dbsystem.models_mysql import *


def index(request):
    return HttpResponse("Hello, world. You're at the dbsystem index.")


def IdConfigure(request):
    return HttpResponse("return an id 2 entity relation map")


def Students2Problem(request):
    exercise_id = request.POST.get('exercise_number')
    print(exercise_id)
    if exercise_id == "-1":
        print("here")
    return render(request, 'Students2Problem.html', {'posts':'here'})
    
