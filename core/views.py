from django.shortcuts import render
from django.shortcuts import render
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from .serializers import TaskSerializer
# Task model
from .models import ProgramItem

@csrf_exempt
def ProgramItems(request):
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
    return render(request=request,
                  template_name='main/homepage.html',
                  context={})
