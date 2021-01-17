from django.shortcuts import render, get_object_or_404
from .models import Appointment, HospitalAppointment
from apps.user.models import CustomUser

# Create your views here.


def consult(request, doctor_pk):
    doctor = get_object_or_404(CustomUser, pk=doctor_pk)
    return render(request, 'appointment/consult.html', {'doctor': doctor})


def appointment(request, doctor_pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        query = request.POST.get('query')
        mobile = request.POST.get('mobile')

        # creating object
        entry = Appointment()
        entry.doctor = CustomUser.objects.get(pk=doctor_pk)
        entry.name = name
        entry.gender = gender
        entry.age = age
        entry.query = query
        entry.mobile = mobile
        entry.status = 'Not Done'
        entry.save()
        print("post doctor_pk: ", doctor_pk)
        # print("post testkey: ", testkey)
        return render(request, 'appointment/appointment.html', {'doctor_pk': doctor_pk})

    else:
        doctor = get_object_or_404(CustomUser, pk=doctor_pk)
        return render(request, 'appointment/consult.html', {'doctor': doctor})


def book(request, doctor_pk):
    doctor = get_object_or_404(CustomUser, pk=doctor_pk)
    return render(request, 'appointment/book-appointment.html', {'doctor': doctor})


def done(request, doctor_pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        appointment_on = request.POST.get('appointment_on')

        # creating object
        entry = HospitalAppointment()
        entry.doctor = CustomUser.objects.get(pk=doctor_pk)
        entry.name = name
        entry.gender = gender
        entry.age = age
        entry.mobile = mobile
        entry.appointment_on = appointment_on
        entry.save()
        print("post doctor_pk: ", doctor_pk)
        # print("post testkey: ", testkey)
        return render(request, 'appointment/done.html', {'doctor_pk': doctor_pk})
