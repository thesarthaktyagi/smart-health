from django.urls import path, include

urlpatterns = [
    path('', include('apps.hospital.urls')),
    path('medicine/<int:hospital_pk>', include('apps.medicine.urls')),
    path('medicine/', include('apps.medicine.urls')),
    path('ai/', include('apps.ai.urls')),

]
