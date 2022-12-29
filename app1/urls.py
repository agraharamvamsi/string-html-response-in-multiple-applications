from django.urls import path
from app1.views import *
app_name='something new'
urlpatterns=[
    path('sujitha/',sujitha,name='sujitha'),
    path('meena/',meena,name='meena'),
]