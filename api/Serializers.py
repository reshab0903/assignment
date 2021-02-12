from rest_framework import serializers
from .models import  User, ActivityPeriod

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('user_id','real_name','tz')

class ActivityPeriodSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields =("User","start_time","end_time")