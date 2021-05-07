from django.urls import path
from .views import *

urlpatterns = [
    path('validate',validateUser),
    path('userData',userData),
    path('msg/<str:convo>',msgData),
    path('Insertrecord',Insertrecord)
]
