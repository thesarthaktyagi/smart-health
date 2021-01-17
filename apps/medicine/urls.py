from django.urls import path, include
from .views import showMedicines, order, postorder

urlpatterns = [
    path('', showMedicines, name='show-medicines'),
    path('order/<int:hospital_pk>/<int:medicine_pk>', order, name='order'),
    path('order/post-order/<int:hospital_pk>/<int:medicine_pk>',
         postorder, name='post-order'),
]
