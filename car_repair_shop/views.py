from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from car_repair_shop.models import Master, Client
from car_repair_shop.forms import RegistrationForm, OrderForm


def start_page(request):
    return render(request, 'index.html')


class Register(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


def list_masters(request):
    return render(request, 'masters.html', {'masters': Master.objects.all()})


def order(request):
    form_initial = {}
    if request.user.is_authenticated:
        client = Client.objects.get(user_id=request.user.id)
        form_initial = {'client_name': client.name,
                        'client_lastname': client.last_name,
                        'client_patronymic': client.patronymic,
                        'client_phone': client.phone_number
                        }
    order_form = OrderForm(initial=form_initial)
    return render(request, 'order.html', {'form': order_form})


def make_order(request):
    pass
