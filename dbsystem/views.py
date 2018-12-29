from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from dbsystem.models_mysql import *


def index(request):
    return HttpResponse("Hello, world. You're at the dbsystem index.")
