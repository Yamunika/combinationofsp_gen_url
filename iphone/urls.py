from django.urls import path
from iphone.views import *
urlpatterns=[
    path('phone/',phone,name='phone'),
    path('iphone/',iphone,name='iphone'),
    
]