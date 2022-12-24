from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser, UserManager


class Car (models.Model):
    car_numner = models.CharField(max_length=20)
    engine_number = models.CharField(max_length=20)
    brand_name = models.CharField(max_length=20)
    model_number = models.CharField(max_length=20)
    mileage = models.PositiveIntegerField()
    seat_no = models.PositiveIntegerField(
        choices=((2, "TWO"), (3, "THREE"), (4, "FOUR"), (5, 'FIVE'), (6, "SIX")))


class Driver (models.Model):
    adhar_no = models.CharField(max_length=12)
    date_of_birth = models.DateField()
    address = models.TextField()
    driving_experience = models.PositiveIntegerField(default=1)
    licens_no = models.CharField(max_length=15)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)


class Passenger(models.Model):
    address = models.TextField(null=True)
    schedule = models.DateTimeField(null=True)


class UserManagerx(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        passenger = Passenger()
        passenger.save()
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_driver", False)
        extra_fields.setdefault("passenger",passenger)
        extra_fields.setdefault("driver", None)

        # if is_driver and not ("driver" in extra_fields.keys()):
        #     raise "is_driver = True: Driver object is required"
        # elif is_driver and ("driver" in extra_fields.keys()):
        #     extra_fields["driver"].save()
        # elif not is_driver and ("driver" in extra_fields.keys()):
        #     extra_fields["driver"] = None

        return self._create_user(username, email, password, **extra_fields)


class Userx(AbstractUser):
    is_driver = models.BooleanField('driver status', default=False)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, null=True)
    passenger = models.OneToOneField(
        Passenger, on_delete=models.CASCADE, null=True)

    objects = UserManagerx()

    def __str__(self) -> str:
        return self.username
