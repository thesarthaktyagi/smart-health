from django.contrib import admin
from .models import Appointment, HospitalAppointment

# Register your models here.


class AppointmentDataAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'doctor', 'gender',
                       'age', 'query', 'mobile', 'time', 'status')


admin.site.register(Appointment, AppointmentDataAdmin)


class HospitalAppointmentDataAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'doctor', 'gender',
                       'age', 'mobile', 'time', 'appointment_on')


admin.site.register(HospitalAppointment, HospitalAppointmentDataAdmin)
