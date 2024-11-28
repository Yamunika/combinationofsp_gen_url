from django.urls import path
from samsung.views import *
urlpatterns=[
    path('phone/',phone,name='phone'),
    path('samsung/',samsung,name='samsung'),
    
]