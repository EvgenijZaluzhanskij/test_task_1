# Generated by Django 2.1.7 on 2019-03-21 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_shop', '0002_auto_20190321_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='master',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
