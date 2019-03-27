from django.db import models

from car_repair_shop.validators import time_validator


class Client(models.Model):
    """
    Client model
    """
    name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    patronymic = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=15, default='')
    user_id = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.last_name + ' ' + self.patronymic


class Master(models.Model):
    """
    Master model
    """
    name = models.CharField(max_length=50, null=False, default='')
    last_name = models.CharField(max_length=50, null=False, default='')

    def __str__(self):
        return self.name + ' ' + self.last_name


class Order(models.Model):
    """
    Order model
    """
    order_status_choices = [
        ('0', 'planning'),
        ('1', 'complete'),
        ('-1', 'canceled')
    ]

    client_id = models.ForeignKey(
        Client,
        on_delete=models.DO_NOTHING,
        default=-1
    )
    master_id = models.ForeignKey(
        Master,
        on_delete=models.DO_NOTHING
    )
    car_model = models.CharField(max_length=50, default='')
    task_type = models.CharField(max_length=50, default='')
    order_status = models.TextField(
        null=False,
        choices=order_status_choices,
        default='0'
    )
    order_plan_date = models.DateField()
    order_plan_time = models.TimeField(validators=[time_validator])
    order_plan_end_time = models.TimeField()
    order_take_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_id.name + ' ' + self.client_id.last_name

    def save(self, *args, **kwargs):
        check_masters = Order.objects.filter(order_plan_time__lte=self.order_plan_time,
                                             order_plan_end_time__gt=self.order_plan_time,
                                             master_id_id=self.master_id,
                                             order_plan_date=self.order_plan_date,
                                             order_status='0')
        if check_masters:
            return False

        super().save(*args, **kwargs)
        return True
