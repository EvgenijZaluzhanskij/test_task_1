from django.db import models


class Client(models.Model):
    """
    Client model
    """
    name = models.CharField(max_length=50, null=False, default='')
    last_name = models.CharField(max_length=50, null=False, default='')
    patronymic = models.CharField(max_length=50, null=False, default='')
    email = models.CharField(max_length=50, null=False, default='')
    phone_number = models.CharField(max_length=15, null=False, default='')
    user_id = models.IntegerField(unique=True, default=0)

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
    car_model = models.CharField(max_length=50, null=False, default='')
    task_type = models.CharField(max_length=50, null=False, default='')
    order_plan_time = models.DateTimeField()
    order_take_time = models.DateTimeField(auto_now_add=True)
    order_status = models.TextField(
        null=False,
        choices=order_status_choices
    )

    def __str__(self):
        return self.client_id.name + ' ' + self.client_id.last_name
