# Generated by Django 2.1.7 on 2019-03-21 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('lastname', models.TextField(blank=True)),
                ('phone_number', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('lastname', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_plan_time', models.DateTimeField()),
                ('order_take_time', models.DateTimeField()),
                ('order_status', models.TextField(blank=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='car_repair_shop.Client')),
                ('master_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='car_repair_shop.Master')),
            ],
        ),
    ]
