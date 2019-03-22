from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from car_repair_shop.models import Client


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
