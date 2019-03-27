import datetime

from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from car_repair_shop.models import Master, Client, Order
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
        try:
            client = Client.objects.get(user_id=request.user.id)
            form_initial = {'name': client.name,
                            'lastname': client.last_name,
                            'patronymic': client.patronymic,
                            'phone': client.phone_number
                            }
        except Client.DoesNotExist:
            pass
    model = Order
    order_form = OrderForm(initial=form_initial)
    return render(request, 'order.html', {'form': order_form, 'model': model})


def make_order(request):
    if request.method == 'POST':
        email = request.POST['email']
        client = Client.objects.get_or_create(email=email, defaults={'name': request.POST['name'],
                                                                     'last_name': request.POST['lastname'],
                                                                     'patronymic': request.POST['patronymic'],
                                                                     'email': email,
                                                                     'user_id': 0})[0]

        plan_time = ':'.join(part for part in [request.POST['plan_time_hours'], request.POST['plan_time_minutes']])

        end_hours = str(int(request.POST['plan_time_hours']) + 1)
        plan_time_end = ':'.join(part for part in [end_hours, request.POST['plan_time_minutes']])
        plan_date = request.POST['order_plan_date']

        order_result = Order(order_plan_time=plan_time,
                             order_plan_end_time=plan_time_end,
                             order_status='0',
                             client_id=client,
                             master_id_id=request.POST['master_id'],
                             car_model=request.POST['car_model'],
                             task_type=request.POST.get('task_type', ''),
                             order_plan_date=plan_date).save()
        if not order_result:
            messages.error(request, 'Master is busy on this time. Please select another time or another master.')
            order_form = OrderForm
            model = Order
            return render(request, 'order.html', {'form': order_form, 'model': model})
        else:
            messages.success(request, 'Order succsessfully created')
            return render(request, 'index.html')

