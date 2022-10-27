from django.http import HttpResponse
from django.shortcuts import render

def frontend(request):
  return HttpResponse(render(request, 'vue_index.html'))