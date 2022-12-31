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




class UserManagerx(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not bool(email) :           
            raise ValueError("The given email must be set")
        if not bool(password) :           
            raise ValueError("The given password must be set")

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_driver", False)  
        extra_fields.setdefault("address", None)  
        extra_fields.setdefault("schedule", None)  
        extra_fields.setdefault("driver", None)   
        return self._create_user(username, email, password, **extra_fields)
        
    def create(self, **validateData):
        username = validateData["username"]; del validateData["username"]
        email = validateData["email"]; del validateData["email"]
        password = validateData["password"] ; del validateData["password"]
        return self.create_user(username, email, password, **validateData)

class Userx(AbstractUser):
    email = models.EmailField("email address", unique=True)
    address = models.TextField(null=True)
    schedule = models.DateTimeField(null=True)
    is_driver = models.BooleanField('driver status', default=False)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, null=True)    

    # REQUIRED_FIELDS=['password']
    objects = UserManagerx()

    def __str__(self) -> str:
        return self.username
