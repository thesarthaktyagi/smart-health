from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='hospital_home'),
    path('<int:hospital_pk>/', views.viewHospital, name='view_hospital'),
    path('department/<int:hospital_pk>/',
         views.department, name='view_department'),
    path('doctor/<int:hospital_pk>/<int:department_pk>/',
         views.viewDoctor, name='doctor'),
]
