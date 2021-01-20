from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
import random
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser
from apps.appointment.models import Appointment, HospitalAppointment
from apps.medicine.models import Order
from apps.hospital.models import Hospital


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))


def signin(request):
    if not request.method == 'POST':
        return render(request, 'user/login.html')

    email = request.POST['email']
    password = request.POST['password']

    # Validation Part
    if not re.match('^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', email):
        return render(request, 'user/login.html', {'form': AuthenticationForm(), 'error': 'Please enter valid email'})

    if len(password) < 3:
        return render(request, 'user/login.html', {'form': AuthenticationForm(), 'error': 'Please provide full length password'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=email)

        if user.check_password(password):
            usr_dict = UserModel.objects.filter(
                email=email).values().first()
            usr_dict.pop('password')

            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return render(request, 'user/login.html', {'form': AuthenticationForm(), 'error': 'You have been logged out. Please login again'})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return redirect('hospital_home')

        else:
            return render(request, 'user/login.html', {'form': AuthenticationForm(), 'error': 'Invalid password'})

    except UserModel.DoesNotExist:
        return render(request, 'user/login.html', {'form': AuthenticationForm(), 'error': 'Email does not exist'})


def signup(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html', {'form': CustomUserCreationForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = CustomUser.objects.create(email=request.POST['email'])
                user.set_password(request.POST['password1'])
                token = generate_session_token()
                user.session_token = token
                user.save()
                login(request, user)
                return redirect('hospital_home')
            except IntegrityError:
                return render(request, 'user/signup.html', {'form': CustomUserCreationForm(), 'error': 'The username is already taken. Please choose another username'})

        else:
            return render(request, 'user/signup.html', {'form': CustomUserCreationForm(), 'error': 'The Passwords did not match'})


@login_required
def signout(request):
    email = request.user.email
    logout(request)

    UserModel = get_user_model()
    hospitals = Hospital.objects.all()

    try:
        user = CustomUser.objects.get(email=email)
        user.session_token = '0'
        user.save()
    except UserModel.DoesNotExist:
        return render(request, 'user/login.html', {'form': AuthenticationForm(), 'error': 'Invalid user'})

    return render(request, 'hospital/index.html', {'form': AuthenticationForm(), 'hospitals': hospitals, 'error': 'Successfully logged out'})


def profile(request):
    if request.user.session_token != '0':
        user = get_object_or_404(CustomUser, email=request.user.email)
        appointments = Appointment.objects.all().filter(email=user.email)
        hospital_appointment = HospitalAppointment.objects.all().filter(email=user.email)
        orders = Order.objects.all().filter(email=user.email)

        return render(request, 'user/profile.html', {'user': user, 'appointment': appointments, 'hospital_appointment': hospital_appointment, 'orders': orders})
    else:
        return redirect('signin')
