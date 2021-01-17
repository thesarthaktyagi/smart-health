from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.hospital.models import Hospital, Department


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=254, unique=True)
    username = None
    hospital = models.ForeignKey(
        Hospital, on_delete=models.SET_NULL, blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, blank=True, null=True)
    is_doctor = models.BooleanField(default=False)
    is_medical_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    speciality = models.TextField(max_length=20, blank=True)
    about = models.TextField(max_length=50, blank=True)
    image = models.ImageField(
        upload_to='hospital/doctors/', blank=True, null=True)

    session_token = models.CharField(max_length=10, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
