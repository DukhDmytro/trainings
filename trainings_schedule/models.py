from django.db import models


class Training(models.Model):
    """
    Class representing training
    """
    name = models.CharField(max_length=200)
    date = models.DateField('training_date')
    time = models.TimeField('training_time')

    def __repr__(self):
        return f'Training: {self.name}'

    def __str__(self):
        return f'Training: {self.name}'
