from django.shortcuts import render_to_response,get_object_or_404
from datetime import datetime
from principal.models import *

import time
from datetime import date
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render_to_response('index.html')
def usuarios(request):
    users = Usuario.objects.all()
    print users
    return render_to_response('usuario.html',{'users':users})