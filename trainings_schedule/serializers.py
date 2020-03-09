import datetime
from rest_framework import serializers

from .models import Training


class TrainingsSerializer(serializers.ModelSerializer):
    """
    Serializer for Training model
    """
    date = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d'])
    time = serializers.TimeField(format="%H:%M", input_formats=['%H:%M'])

    class Meta:
        model = Training
        fields = 'name', 'date', 'time',

    def validate_date(self, date):
        """
        Check that date is correct. Accept dates that are today or future dates.
        :param date:
        :return: date if valid
        :raise Validation error in case of incorrect date
        """
        if date < datetime.date.today():
            raise serializers.ValidationError('You can add training only for today or future dates')
        return date

    def validate_time(self, time):
        """
        Check that time is correct. Accept future time.
        :param time:
        :return: time if valid
        :raise Validation error in case of incorrect time
        """
        data = self.get_initial()
        if time < datetime.datetime.now().time() and data['date'] == datetime.date.today().strftime("%Y-%m-%d"):
            raise serializers.ValidationError('This time already passed')
        return time
