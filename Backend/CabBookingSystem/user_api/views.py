from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.views import ObtainAuthToken

from .models import Userx
from user_api.serializers import UserxSerializers
# Create your views here.


# class Login(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})


@api_view(['post'])
def user_login(req):
    data = req.data
    user = Userx.objects.get(username=data["username"])
    serializer = UserxSerializers(user)
    token, created = Token.objects.get_or_create(user=user)
    data = serializer.data
    print(token, created)
    data["token"] = token.key
    print(data, serializer.data)
    return Response(data)


@api_view(['post'])
def user_signup(req):
    serializer = UserxSerializers(req.data)
    data = serializer.data
    return Response(data)


@api_view(['post'])
def user_profile(req):
    print(req.user)
    return Response({})


def user_history(req):
    pass


def user_schedule(req):
    pass


def driver_profile(req):
    pass


def driver_history(req):
    pass


def driver_car_detail(req):
    pass


@api_view(['post'])
def driver_registration(req):
    pass


@api_view(['post'])
def driver_login(req):
    pass
