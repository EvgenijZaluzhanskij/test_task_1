# Generated by Django 2.1.7 on 2019-03-26 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_shop', '0010_auto_20190326_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_plan_end_time',
            field=models.TimeField(),
        ),
    ]
