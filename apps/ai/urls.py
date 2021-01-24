from django.urls import path, include
from . import views

urlpatterns = [
    path('cancer', views.cancer, name='cancer'),
    path('cancer-result', views.predict, name='cancer-result'),
    path('heart', views.heart, name='heart'),
    path('heart-result', views.heartPredict, name='heart-result'),
    path('diabetes', views.diabetes, name='diabetes'),
    path('diabetes-result', views.diabetesPredict, name='diabetes-result'),
    path('kidney', views.kidney, name='kidney'),
    path('kidney-result', views.kidneyPredict, name='kidney-result'),
    path('liver', views.liver, name='liver'),
    path('liver-result', views.liverPredict, name='liver-result'),

]
