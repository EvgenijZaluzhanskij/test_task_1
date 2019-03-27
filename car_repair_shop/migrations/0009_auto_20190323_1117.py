# Generated by Django 2.1.7 on 2019-03-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_shop', '0008_auto_20190323_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_plan_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_plan_end_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_plan_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
