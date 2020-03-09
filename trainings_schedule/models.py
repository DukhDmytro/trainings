import datetime
from django.db import models
from django.core.exceptions import ValidationError


class Training(models.Model):
    """
    Class representing training
    """
    name = models.CharField(max_length=200)
    date = models.DateField('Training date')
    time = models.TimeField('Training time')

    def __repr__(self):
        return f'Training: {self.name}'

    def __str__(self):
        return f'Training: {self.name}'

    def clean(self):
        """
        Check that date and time are correct. Accept dates and time that are today now or future dates and time.
        """
        try:
            if self.date < datetime.date.today():
                raise ValidationError('You can add training only for today or future dates')
            if self.time < datetime.datetime.now().time() and self.date == datetime.date.today():
                raise ValidationError('This time already passed')
        except TypeError:
            raise ValidationError('Incorrect value of date or time')
