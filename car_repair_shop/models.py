from django.db import models


class Client(models.Model):
    """
    Client model
    """
    name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.name + ' ' + self.last_name


class Master(models.Model):
    """
    Master model
    """
    name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name + ' ' + self.last_name


class Order(models.Model):
    """
    Order model
    """
    order_status_choices = [
        (0, 'planning'),
        (1, 'complete'),
        (-1, 'canceled')
    ]

    client_id = models.OneToOneField(
        Client,
        on_delete=models.DO_NOTHING
    )
    master_id = models.ForeignKey(
        Master,
        on_delete=models.DO_NOTHING
    )
    order_plan_time = models.DateTimeField(null=False)
    order_take_time = models.DateTimeField(auto_now_add=True)
    order_status = models.TextField(
        null=False,
        choices=order_status_choices
    )

