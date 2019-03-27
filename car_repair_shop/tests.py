from django.test import TestCase

from car_repair_shop.models import Order, Client, Master


class OrderTestCase(TestCase):
    def setUp(self):
        Master.objects.create(name="First", last_name="Master")
        Master.objects.create(name="Second", last_name="Master")

        Client.objects.create(name='First',
                              last_name='Test',
                              patronymic='Client',
                              email='email1@mail.ru')
        Client.objects.create(name='Second',
                              last_name='Test',
                              patronymic='Client',
                              email='email2@mail.ru')

    def test_create_order(self):
        """Ordinary create order without time troubles"""
        master = Master.objects.get(name="First", last_name='Master')
        client = Client.objects.get(email="email1@mail.ru")

        self.assertTrue(Order(order_plan_time='10:00',
                              order_plan_end_time='11:00',
                              order_status='0',
                              client_id=client,
                              master_id_id=master.pk,
                              car_model='Tesla',
                              task_type='Diagnostic',
                              order_plan_date='2019-01-01').save())

    def test_create_order_with_time_conflict(self):
        """Create order with time conflict with previous order"""
        master = Master.objects.get(name="First", last_name='Master')
        client = Client.objects.get(email="email1@mail.ru")
        client2 = Client.objects.get(email="email2@mail.ru")

        first_order = Order(order_plan_time='10:00',
                            order_plan_end_time='11:00',
                            order_status='0',
                            client_id=client,
                            master_id_id=master.pk,
                            car_model='Tesla',
                            task_type='Diagnostic',
                            order_plan_date='2019-01-01').save()

        self.assertFalse(Order(order_plan_time='10:30',
                               order_plan_end_time='11:30',
                               order_status='0',
                               client_id=client2,
                               master_id_id=master.pk,
                               car_model='Vaz',
                               task_type='Diagnostic',
                               order_plan_date='2019-01-01').save())


