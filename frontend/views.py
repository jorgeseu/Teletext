from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
#sem comentario
def frontend(request):
  return HttpResponse(render(request, 'vue_index.html'))