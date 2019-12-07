from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .forms import *


def client(request):
    form = Client()
    return render(request, 'solarpv/client_form.html', {'form': form})

def location(request):
    form = Location()
    return render(request, 'solarpv/location_form.html', {'form': form})

def product(request):
    form = Product()
    return render(request, 'solarpv/product_form.html', {'form': form})

def teststandard(request):
    form = Test_Standard()
    return render(request, 'solarpv/teststandard_form.html', {'form': form})

def certificate(request):
    form = Certificate()
    return render(request, 'solarpv/certificate_form.html', {'form': form})

def index(request):
    return render(request, 'solarpv/index.html')


def aboutus(request):
    return render(request, 'solarpv/aboutus.html')


def portal(request):
    return render(request, 'solarpv/form.html')


def register(request):
    form = User()
    return render(request, 'solarpv/registrationform.html', {'form': form})
