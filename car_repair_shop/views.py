from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from car_repair_shop.models import Master
from car_repair_shop.forms import RegistrationForm


def start_page(request):
    return render(request, 'index.html')


class Register(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


def list_masters(request):
    return render(request, 'masters.html', {'masters': Master.objects.all()})


def make_order(request):
    pass
