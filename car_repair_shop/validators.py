import datetime
from django.core.exceptions import ValidationError


restrictions = {'min_time': datetime.time(hour=10, minute=0, second=0),
                'max_time': datetime.time(hour=20, minute=0, second=0),
                'weekends': [5, 6]}


def time_validator(value):
    if value < restrictions['min_time'] or value > restrictions['max_time'] or \
            value.replace(hour=value.hour + 1) > restrictions['max_time']:
        raise ValidationError(
            ('Order time must be between 10:00 and 20:00'),
            params={'value': value},
        )
