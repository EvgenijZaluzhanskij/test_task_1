from django.shortcuts import render

from car_repair_shop.models import Master


def start_page(request):
    return render(request, 'index.html')


def list_masters(request):
    return render(request, 'masters.html', {'masters': Master.objects.all()})
