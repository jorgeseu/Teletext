from django.shortcuts import render
from .serializers import AnnoucementSerializer
from .models import Annoucement
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class AnnoucementViev(APIView):
    #only if is authenticated can create or if is not, allow to read data
    permission_classes = (IsAuthenticatedOrReadOnly,)

    #get request income do this
    def get(self, request):
        #only accepted annoucement
        annoucement = Annoucement.objects.filter(annoucement_status = 'accepted')
        serializer = AnnoucementSerializer(annoucement, many = True)
        return Response(serializer.data)

    #post request, to create do this
    def post(self,request):
        serializer = AnnoucementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)