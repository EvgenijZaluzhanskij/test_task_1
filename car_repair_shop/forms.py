from django import forms
from django.contrib.auth.forms import UserCreationForm

from car_repair_shop.models import Client, Master, Order


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


class OrderForm(forms.ModelForm):
    name = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    patronymic = forms.CharField(required=True)
    email = forms.CharField(required=True)
    master_id = forms.ModelChoiceField(Master.objects.all())
    car_model = forms.CharField(required=True)
    task_type = forms.CharField()
    order_plan_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    # Мне это место очень не нравится - я честно пытался сделать нормальный выбор времени,
    # но у меня никак не завелось ни с какими виджетами
    # даже на стеке спрашивал - там не ответили
    # https://stackoverflow.com/questions/55314221/input-time-with-custom-form-trouble
    CHOICES_HOURS = tuple(
        (
            '0%s' % x if x < 10 else '%s' % x,
            '0%s' % x if x < 10 else '%s' % x,
        ) for x in range(10, 20)
    )
    plan_time_hours = forms.TimeField(label='hours', widget=forms.Select(choices=CHOICES_HOURS))

    CHOICES_MINUTES = tuple(
        (
            '0%s' % x if x < 10 else '%s' % x,
            '0%s' % x if x < 10 else '%s' % x,
        ) for x in range(0, 60)
    )
    plan_time_minutes = forms.TimeField(label='minutes', widget=forms.Select(choices=CHOICES_MINUTES))

    def save(self):
        pass

    class Meta:
        model = Order
        fields = ('name', 'lastname', 'patronymic', 'email', 'task_type', 'order_plan_date',
                  'plan_time_hours', 'plan_time_minutes', 'master_id',  'car_model')

