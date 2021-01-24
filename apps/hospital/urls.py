from django.urls import path, include
from . import views
from apps.appointment.views import consult, appointment, book, done
from apps.hospital.views import callAppointment, hospitalAppointment

urlpatterns = [
    path('', views.home, name='hospital_home'),
    path('<int:hospital_pk>/', views.viewHospital, name='view_hospital'),
    path('department/<int:hospital_pk>/',
         views.department, name='view_department'),
    path('doctor/<int:hospital_pk>/<int:department_pk>/',
         views.viewDoctor, name='doctor'),
    path('reserve/<int:hospital_pk>/',
         views.reserve, name='reserve'),
    path('success/<int:hospital_pk>/',
         views.success, name='success'),
    path('consult/<int:doctor_pk>/', consult, name='consult'),
    path('appointment/<int:doctor_pk>/', appointment, name='appointment'),
    path('book-appointment/<int:doctor_pk>/', book, name='book-appointment'),
    path('done/<int:doctor_pk>/', done, name='done'),
    path('mark/<int:appointment_pk>/', callAppointment, name='callAppointment'),
    path('marked/<int:appointment_pk>/',
         hospitalAppointment, name='hospitalAppointment'),
]
