from rest_framework import serializers
from .models import Car, Driver, Passenger, Userx


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'car_numner', 'engine_number', 'brand_name',
            'model_number', 'mileage', 'seat_no',
        ]


class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'adhar_no', 'date_of_birth', 'address',
            'driving_experience', 'licens_no',
        ]


class PassengerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ["address", "schedule", ]


class UserxSerializers(serializers.ModelSerializer):
    # driver = DriverSerializers()
    # passenger = PassengerSerializers()

    class Meta:
        model = Userx

        fields = [
            'first_name', 'last_name', 'email',
            'username', 'is_driver', 'driver', 'passenger','password'

        ]
        extra_kwargs={
            'password':{"write_only":True, "required":True}
        }

        # depth = 1
