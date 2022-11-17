from django.shortcuts import render
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
# API definition for task
from .serializers import TaskSerializer
# Task model
from .models import ProgramItem

#gfauth
import httplib2
from googleapiclient.discovery import build
from teletext import settings
#from oauth2client.contrib import xsrfutil
#from oauth2client.client import flow_from_clientsecrets
#from oauth2client.contrib.django_util.storage import DjangoORMStorage
from httplib2 import Http
from teletext_helper import Fetching_current_data


@csrf_exempt
def ProgramItems(request):
  Prog_it = Fetching_current_data()
  Prog_it.fetch_data()
  if(request.method == 'GET'):
    #get all program data
    ProgramItems = ProgramItem.objects.all()
    #serialize the task data
    serializer = TaskSerializer(ProgramItems, many=True)
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
      #provide json respo with data that was saved
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def Program_detail(request, pk):
  try:
    #obtain the task with the passed id
    ProgramItem = ProgramItem.objects.get(pk=pk)
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
# Create your views here.
def homepage(request):
  # status = True
  #
  # if not request.user.is_authenticated:
  #   return HttpResponseRedirect('admin')
  #
  # storage = DjangoORMStorage(gCredentialsModel, 'id', request.user, 'credential')
  # credential = storage.get()
  # try:
  #   access_token = credential.access_token
  #   resp, cont = Http().request("https://www.googleapis.com/auth/gmail.readonly",
  #                               headers={'Host': 'www.googleapis.com',
  #                                        'Authorization': access_token})
  # except:
  #   status = False
  #   print('Not Found')

  return render(request=request, template_name='main/homepage.html', context={})


#GMAIL API IMPLEMENTATION

# FLOW = flow_from_clientsecrets(
#     settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
#     scope='https://www.googleapis.com/auth/gmail.readonly',
#     redirect_uri='http://http://45.9.188.43:9090//oauth2callback', # do zmiany przy starcie na PRD
#     prompt='consent')

# def gmail_authenticate(request):
#   storage = DjangoORMStorage(gCredentialsModel, 'id', request.user, 'credential')
#   credential = storage.get()
#   if credential is None or credential.invalid:
#     FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
#                                                    request.user)
#     authorize_url = FLOW.step1_get_authorize_url()
#     return HttpResponseRedirect(authorize_url)
#   else:
#     http = httplib2.Http()
#     http = credential.authorize(http)
#     service = build('gmail', 'v1', http=http)
#     print('access_token = ', credential.access_token)
#     status = True
#
#     return render(request, 'main/homepage.html', {'status': status})
#
# def auth_return(request):
#   get_state=bytes(request.GET.get('state'), 'utf-8')
#   if not xsrfutil.validate_token(settings.SECRET_KEY, get_state,
#                                  request.user):
#     return HttpResponseBadRequest()
#   credential = FLOW.step2_exchange(request.GET.get('code'))
#   storange = DjangoORMStorage(gCredentialsModel, 'id', request.user, 'credential')
#   storange.put(credential)
#   print("access_token: %s" % credential.access_token)
#   return HttpResponseRedirect("/")