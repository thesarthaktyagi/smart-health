from django.shortcuts import render, redirect, get_object_or_404
from .models import Hospital, Department, Doctor
from apps.user.models import CustomUser
import razorpay


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
    doctors = CustomUser.objects.filter(
        hospital__pk=hospital_pk, department__pk=department_pk)
    print(request, hospital_pk, department_pk)
    return render(request, 'hospital/doctors.html', {'doctors': doctors})


def reserve(request, hospital_pk):
    if request.method == 'POST':
        amount = 100
        order_currency = 'INR'
        client = razorpay.Client(
            auth=('rzp_test_C7uQQW33qnlN7U', 'cloa5wsBOitpGfzdtseoJdoB'))
        payment = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    hospital = get_object_or_404(Hospital, pk=hospital_pk)
    return render(request, 'hospital/reserve.html', {'hospital': hospital})


def success(request, hospital_pk):
    hospital = get_object_or_404(Hospital, pk=hospital_pk)
    hospital.beds_available -= 1
    hospital.save()

    return render(request, 'hospital/success.html', {'hospital': hospital})
