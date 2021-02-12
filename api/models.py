from django.db import models
from _datetime import datetime

class User(models.Model):
    user_id = models.CharField(max_length= 30, primary_key=True)
    real_name = models.CharField(max_length = 30 )
    tz = models.CharField(max_length = 30)

    def __str__(self):
        return self.user_id
    class Meta:
        db_table='USER'
class ActivityPeriod(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now, blank=False)
    end_time = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.User
    class Meta:
        db_table='ActivityPeriod'