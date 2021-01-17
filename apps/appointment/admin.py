from django.contrib import admin
from .models import Appointment

# Register your models here.


class AppointmentDataAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'doctor', 'gender',
                       'age', 'query', 'mobile', 'time')


admin.site.register(Appointment, AppointmentDataAdmin)
