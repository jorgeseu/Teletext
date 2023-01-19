
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, GetUserDetailsSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import  MyTokenObtainPairSerializer
from .models import UserData

from annoucement.models import Annoucement
from annoucement.serializers import AnnoucementSerializer
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, request
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
#stats
from core.stats_helper import store_user_action


# Create your views here.

# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # stats
            store_user_action('Unlogged', 'User Registered')
            serializer.save()
            return Response({"detail": "success"},status=status.HTTP_201_CREATED)


        # responce detail info and  http status
        return Response({"detail": "fail"},status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserDetail(generics.RetrieveAPIView):
   # permission_classes = (IsAuthenticated,)

    queryset = UserData.objects.values('id', 'email', 'name')
    serializer_class = GetUserDetailsSerializer


class UserAnnoucements(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):

        user = request.user.id
        queryset = Annoucement.objects.filter(user_id=user)
        serializer_class = AnnoucementSerializer(queryset, many=True)
        return Response(serializer_class.data)




    # def get_object(self):
    #     id =
    #     username = self.kwargs.get("username")
    #     email = self.kwargs.get("email")
    #     return id,username,email


# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)