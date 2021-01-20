from django.db import models
from apps.hospital.models import Hospital


class Medicine(models.Model):
    hospital = models.ForeignKey(
        Hospital, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.TextField(max_length=25)
    company = models.TextField(max_length=25)
    description = models.TextField(max_length=40)
    in_stock = models.BooleanField(default=True)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='medicine/images/')

    def __str__(self):
        return self.name.upper() + '--' + str(self.hospital)


class Order(models.Model):
    name = models.TextField(max_length=30)
    email = models.EmailField(blank=True)
    hospital = models.TextField(max_length=30)
    quantity = models.IntegerField()
    address = models.TextField(max_length=50)
    mobile = models.IntegerField()
    prescription = models.URLField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.time)+'--'+self.hospital
