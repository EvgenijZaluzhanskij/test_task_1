from django import forms
from django.contrib.auth.forms import UserCreationForm

from car_repair_shop.models import Client, Master


class RegistrationForm(UserCreationForm):
    name = forms.CharField(label="Name", required=True, max_length=50)
    last_name = forms.CharField(label="Last name", required=True, max_length=50)
    patronymic = forms.CharField(label="Patronymic", required=True, max_length=50)
    phone = forms.CharField(label="Phone number", required=True, max_length=50)
    email = forms.CharField(label="Email", required=True, max_length=50)

    def save(self, commit=True):
        user = super().save(commit)

        new_client = Client(name=self.cleaned_data['name'],
                            last_name=self.cleaned_data['last_name'],
                            patronymic=self.cleaned_data['patronymic'],
                            phone_number=self.cleaned_data['phone'],
                            email=self.cleaned_data['email'],
                            user_id=user.id
                            )
        new_client.save()

        return user


class OrderForm(forms.Form):
    client_name = forms.CharField(required=True)
    client_lastname = forms.CharField(required=True)
    client_patronymic = forms.CharField(required=True)
    client_phone = forms.CharField(required=True)
    plan_date = forms.DateTimeField()
    master = forms.ModelChoiceField(Master.objects.all())
    client_car = forms.CharField(required=True)
