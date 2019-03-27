# test_task_1

Simple application for making orders im car repairs shop.


Howto start
1) get project
2) open and install requirements
3) set your database in settings.py
4) python manage.py migrate
5) run


In this simple app you can:
1) Create your own user to simplify ordering
2) Create order by conditions: only in time of working car repair shop (10:00 - 20:00)
3) In admin can edit and create orders


Run tests:
1) python manage.py test

There are 2 major test:
- creating order
- creating order with time conflict on masters

If tests not run with error: permission denied for create database
execute this command on psql shell

ALTER USER <user_name> CREATEDB;

<user_name> - user name from db configuration on settings.py