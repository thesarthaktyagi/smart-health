from django.db import models
from apps.user.models import CustomUser


class Appointment(models.Model):
    doctor = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.TextField(max_length=30)
    gender = models.TextField(max_length=10)
    age = models.IntegerField()
    query = models.TextField(max_length=100)
    mobile = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    status = models.TextField(
        max_length=12, blank=True, null=True, default='Not Done')

    def __str__(self):
        return self.name


class HospitalAppointment(models.Model):
    doctor = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.TextField(max_length=30)
    gender = models.TextField(max_length=10)
    age = models.IntegerField()
    mobile = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    appointment_on = models.DateTimeField()

    def __str__(self):
        return self.name
