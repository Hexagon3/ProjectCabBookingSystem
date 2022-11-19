
from django.urls import path
from .views import *

# localhost:8020
# localhost:8020/user/
# localhost:8020/driver/
urlpatterns = [
    # User
    path('user/profile/', user_profile),                  # Get
    path('user/history', user_history),                   # Get
    path('user/schedule', user_schedule),                 # Get
    path('user/login', user_login),                       # Post
    path('user/signup', user_signup),                     # Post

    # Driver
    path('driver/profile', driver_profile),               # Get
    path('driver/history', driver_history),               # Get
    path('driver/car_detail', driver_car_detail),         # Get
    path('driver/registration', driver_registration),     # Post
    path('driver/login', driver_login),                   # Post

]


# - http://HOST_IP/user_api/user/profile
# - http://HOST_IP/user_api/user/history
# - http://HOST_IP/user_api/user/schedule
# - http://HOST_IP/user_api/user/login
# - http://HOST_IP/user_api/user/signup
# - http://HOST_IP/user_api/driver/profile
# - http://HOST_IP/user_api/driver/history
# - http://HOST_IP/user_api/driver/car_detail
# - http://HOST_IP/user_api/driver/registration
# - http://HOST_IP/user_api/driver/login
