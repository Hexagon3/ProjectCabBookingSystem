from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, authenticate
# from rest_framework.authtoken.views import ObtainAuthToken


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Userx,  Driver
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
    try:
        try:
            username = data["username"]        
            user = Userx.objects.get(username = username)
        except :
            email = data["email"]
            user = Userx.objects.get(email = email)
        finally:
            password=data["password"]          
    except:
        return Response({"status": "Failed"})
    if not user.check_password(password):
        return Response({"status": "Password Not Match"})     
    # serializer = UserxSerializers(user)
    token = get_tokens_for_user(user)
    # data = serializer.data
    # login(req, user)
    data["token"] = token
    # print(data, serializer.data)
    return Response(data)


@api_view(['post'])
def user_signup(req):
    user = None
    serializer = UserxSerializers(data=req.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        print(user)
        data = serializer.data
        data["status"]="Success"
    return Response(data)
@api_view(['get'])
def list_user(req):
    s = Userx.objects.all()


@api_view(['post'])
def user_profile(req):   
    try:
        user = req.user
        print(user)
        serializer = UserxSerializers(user)
        return Response(serializer.data)
    except:
        return Response({"status":"Something Wrong"})


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
