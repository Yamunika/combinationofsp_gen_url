from django.shortcuts import render
from django.http import HttpResponse
def phone(requset):
    return HttpResponse('<h1>in the phones samsung company is the best</h1>')
def samsung(requset):
    return HttpResponse('<h1>samsung company is the second best in the world</h1>')

