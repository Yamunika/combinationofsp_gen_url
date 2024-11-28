from django.shortcuts import render
from django.http import HttpResponse
def phone(request):
    return HttpResponse('<h1> In the phones company iphone is the best</h1>')
def iphone(request):
    return HttpResponse('<h1> iphone is the most costly phone in theworld</h1>')
