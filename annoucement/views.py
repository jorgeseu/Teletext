from django.shortcuts import render
from .serializers import AnnoucementSerializer ,AnnoucementCategorySerializer
from .models import Annoucement , Annoucement_category
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.views.generic.edit import CreateView , DeleteView, UpdateView
#stats
from ..core.stats_helper import store_user_action

# Create your views here.

# class AnnoucementViev(APIView):
#
#     #chenge to by owner in future
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     #get request income do this
#     def get(self, request):
#         #only accepted annoucement
#         annoucement = Annoucement.objects.filter(annoucement_status = 'accepted')
#         serializer = AnnoucementSerializer(annoucement, many = True)
#         return Response(serializer.data)
#
#     #post request, to create do this
#     def post(self,request):
#         serializer = AnnoucementSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)



#get list of categories
class AnnoucementCategory(APIView):

    def get(self, request):
        queryset = Annoucement_category.objects.all()
        serializer = AnnoucementCategorySerializer(queryset, many=True)
        return Response(serializer.data)

#get Annoucements list specify by category, need category id
class AnnoucementsByCategory(APIView):

    def get(self, request, id):
        queryset = Annoucement.objects.filter(category_name=id, annoucement_status = 'accepted' )
        serializer = AnnoucementSerializer(queryset, many=True)
        return Response(serializer.data)

#####
#only if is authenticated can create(post) or if is not, allow to read data
class AnnoucementList(generics.ListCreateAPIView):
    queryset = Annoucement.objects.filter(annoucement_status = 'accepted')
    serializer_class = AnnoucementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#update and delete
#put request to update delete request to delete
#allow only if is owner
class AnnoucementUpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annoucement.objects.all()
    serializer_class = AnnoucementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



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


