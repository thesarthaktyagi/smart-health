from django.db import models
# from apps.user.models import CustomUser


class Hospital(models.Model):
    name = models.TextField(max_length=100)
    image = models.ImageField(upload_to='hospital/images/')
    location = models.TextField(max_length=50, blank=True)
    about = models.TextField(max_length=1000)
    beds_available = models.IntegerField()
    doctors_available = models.IntegerField()

    def __str__(self):
        return self.name


class Department(models.Model):
    hospital = models.ForeignKey(
        Hospital, on_delete=models.SET_NULL, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True)
    about = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.department.upper()+'-'+str(self.hospital)


class Doctor(models.Model):
    name = models.TextField(max_length=30)
    speciality = models.TextField(max_length=40)
    hospital = models.ForeignKey(
        Hospital, on_delete=models.SET_NULL, blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, blank=True, null=True)
    about = models.TextField(max_length=50, blank=True)
    image = models.ImageField(upload_to='hospital/doctors/')

    def __str__(self):
        return self.name.upper()+'--'+str(self.hospital)
