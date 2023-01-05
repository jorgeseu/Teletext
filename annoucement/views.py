from django.shortcuts import render
from .serializers import AnnoucementSerializer ,AnnoucementCategorySerializer
from .models import Annoucement , Annoucement_category
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import generics
from django.views.generic.edit import CreateView , DeleteView, UpdateView

# Create your views here.

class AnnoucementViev(APIView):
    #only if is authenticated can create(post) or if is not, allow to read data
    #chenge to by owner in future
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

    def delete(self, request):
        pass

    def patch(self, request):
        pass

#get list of categories
class AnnoucementCategory(APIView):

    def get(self, request):
        queryset = Annoucement_category.objects.all()
        serializer = AnnoucementCategorySerializer(queryset, many=True)
        return Response(serializer.data)

#get Annoucement i specify category by id
class AnnoucementsByCategory(APIView):

    def get(self, request, id):
        queryset = Annoucement.objects.filter(category_name=id)
        serializer = AnnoucementSerializer(queryset, many=True)
        return Response(serializer.data)


#update and delete temporary
#put request to update delete request to delete
class AnnoucementUpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annoucement.objects.all()
    serializer_class = AnnoucementSerializer



# class AnnoucementDeleteView(DeleteView):
#     # specify the model you want to use
#     model = Annoucement
#
#     # can specify success url
#     # url to redirect after successfully
#     # deleting object
#     success_url = "/"
#
#   #  template_name = "geeks/geeksmodel_confirm_delete.html"
#
# class AnnoucementUpdateView(UpdateView):
#     # specify the model you want to use
#     model = Annoucement
#
#     # specify the fields
#     fields = [
#         "title",
#         "description",
#         "category_name"
#     ]
#
#     # can specify success url
#     # url to redirect after successfully
#     # updating details
#     success_url = "/"


