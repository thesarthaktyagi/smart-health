from django.shortcuts import render, redirect, get_object_or_404
from .models import Hospital, Department, Doctor


def home(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital/index.html', {'hospitals': hospitals})


def viewHospital(request, hospital_pk):
    hospital = get_object_or_404(Hospital, pk=hospital_pk)
    return render(request, 'hospital/hospital.html', {'hospital': hospital})


def department(request, hospital_pk):
    departments = Department.objects.filter(hospital__pk=hospital_pk)
    hospital = get_object_or_404(Hospital, pk=hospital_pk)
    # dep = departments.department.split(',')
    print(request, hospital_pk)
    return render(request, 'hospital/department.html', {'departments': departments, 'hospital': hospital})


def viewDoctor(request, hospital_pk, department_pk):
    doctors = Doctor.objects.filter(
        hospital__pk=hospital_pk, department__pk=department_pk)
    print(request, hospital_pk, department_pk)
    return render(request, 'hospital/doctors.html', {'doctors': doctors})
