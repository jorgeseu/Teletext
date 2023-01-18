from django.shortcuts import render
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
# API definition for task
from .serializers import TaskSerializer, MODSerializer, StatSerializer
# Task model
from .models import ProgramItem, MOD_item
from .stat_models import Action
from .stats_helper import store_user_action

#gfauth
import httplib2
from googleapiclient.discovery import build
from teletext import settings
#from oauth2client.contrib import xsrfutil
#from oauth2client.client import flow_from_clientsecrets
#from oauth2client.contrib.django_util.storage import DjangoORMStorage
from httplib2 import Http
from .teletext_helper import Fetching_current_data
from datetime import date


@csrf_exempt
def ProgramItems(request):
  Prog_it = Fetching_current_data()
  Prog_it.fetch_data()
  if(request.method == 'GET'):
    #get all program data
    ProgramItems = ProgramItem.objects.all()
    #serialize the task data
    serializer = TaskSerializer(ProgramItems, many=True)
    # stat part
    current_user = request.user
    store_user_action(current_user.id, 'Program data request')
    # return a JSON response
    return JsonResponse(serializer.data,safe=False)
  elif(request.method == 'POST'):
    #parse the incoming information
    data= JSONParser().parse(request)
    #new instance with serializer
    serializer = TaskSerializer(data=data)
    #verify sent information
    if(serializer.is_valid()):
      #if ok save it on the DB
      serializer.save()
      # stat part
      current_user = request.user
      store_user_action(current_user.id, 'Program data request')
      #provide json respo with data that was saved
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def Program_detail(request, pk):
  try:
    #obtain the task with the passed id
    ProgramItem = ProgramItems.objects.get(pk=pk)
  except:
    # respond with a 404 error message
    return HttpResponse(status=404)
  if (request.method == 'PUT'):
    # parse the incoming information
    data = JSONParser().parse(request)
    # instanciate with the serializer
    serializer = TaskSerializer(ProgramItem, data=data)
    # check whether the sent information is okay
    if (serializer.is_valid()):
      # if okay, save it on the database
      serializer.save()
      # provide a JSON response with the data that was submitted
      return JsonResponse(serializer.data, status=201)
    # provide a JSON response with the necessary error information
    return JsonResponse(serializer.errors, status=400)
  elif (request.method == 'DELETE'):
    # delete the task
    ProgramItem.delete()
    # return a no content response.
    return HttpResponse(status=204)

def MODItems(request):
  if(request.method == 'GET'):
    MODItems = MOD_item.objects.get(message_date=date.today())
    serializer = MODSerializer(MODItems)
    # stat part
    current_user = request.user
    store_user_action(current_user.id, 'Message of the day request')
    return JsonResponse(serializer.data, safe=False)
def MOD_detail(request, pk):
  try:
    #obtain the task with the passed id
    MODItem = MOD_item.objects.get(pk=pk)
  except:
    # respond with a 404 error message
    return HttpResponse(status=404)
  if (request.method == 'PUT'):
    # parse the incoming information
    data = JSONParser().parse(request)
    # instanciate with the serializer
    serializer = MODSerializer(MOD_item, data=data)
    # check whether the sent information is okay
    if (serializer.is_valid()):
      # if okay, save it on the database
      serializer.save()
      # provide a JSON response with the data that was submitted
      return JsonResponse(serializer.data, status=201)
    # provide a JSON response with the necessary error information
    return JsonResponse(serializer.errors, status=400)
  elif (request.method == 'DELETE'):
    # delete the task
    MOD_item.delete()
    # return a no content response.
    return HttpResponse(status=204)
def StatItems(request):
  if(request.method == 'GET'):
    Stat_items = Action.objects.get(message_date=date.today())
    serializer = StatSerializer(Stat_items)
    return JsonResponse(serializer.data, safe=False)

def Stat_detail(request, pk):
  try:
    #obtain the task with the passed id
    Stat_item = Action.objects.get(pk=pk)
  except:
    # respond with a 404 error message
    return HttpResponse(status=404)
  if (request.method == 'PUT'):
    # parse the incoming information
    data = JSONParser().parse(request)
    # instanciate with the serializer
    serializer = StatSerializer(Stat_item, data=data)
    # check whether the sent information is okay
    if (serializer.is_valid()):
      # if okay, save it on the database
      serializer.save()
      # provide a JSON response with the data that was submitted
      return JsonResponse(serializer.data, status=201)
    else:
    # provide a JSON response with the necessary error information
      return JsonResponse(serializer.errors, status=400)
  else:
    # return a no content response.
    return HttpResponse(status=204)

# Create your views here.
def homepage(request):
  return render(request=request, template_name='main/homepage.html', context={})

def login(request):

  return render(request=request, template_name='main/login.html', context={})