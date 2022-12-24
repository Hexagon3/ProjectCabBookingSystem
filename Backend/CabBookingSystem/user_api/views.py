from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
# from rest_framework.authtoken.views import ObtainAuthToken


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Userx, Passenger, Driver
from user_api.serializers import UserxSerializers
# Create your views here.

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



# User
@api_view(['post'])
def user_login(req):
    data = req.data
    user = Userx.objects.get(username=data["username"])
    serializer = UserxSerializers(user)
    token, created = Token.objects.get_or_create(user=user)
    data = serializer.data
    login(req, user)
    data["token"] = token.key
    print(data, serializer.data)
    return Response(data)


@api_view(['post'])
def user_signup(req):
    user = None
    serializer = UserxSerializers(data=req.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        print(user)
    
    return Response({"status":"Success"})


@api_view(['get'])
def user_profile(req, pk=None):
    if pk is None:
        # user = req.user
        # print(req.user)
        # serializer = UserxSerializers(data= user)
        return Response({})
    user = Userx.objects.get(id=pk)
    serializer = UserxSerializers(user)
    print(pk)
    return Response(serializer.data)


@api_view(['get'])
def user_history(req):
    return Response({})


@api_view(['get'])
def user_schedule(req):
    return Response({})

# Driver


@api_view(['get'])
def driver_profile(req):
    return Response({})


@api_view(['get'])
def driver_history(req):
    return Response({})


@api_view(['get'])
def driver_car_detail(req):
    return Response({})


@api_view(['post'])
def driver_registration(req):
    return Response({})


@api_view(['post'])
def driver_login(req):
    return Response({})
