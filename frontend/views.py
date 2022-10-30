from django.http import HttpResponse
from django.shortcuts import render
#vuejs test only
def frontend(request):
  return HttpResponse(render(request, 'vue_index.html'))