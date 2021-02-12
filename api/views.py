from django.shortcuts import render
from .models import User, ActivityPeriod
from datetime import datetime
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .Serializers import *

DATE_FORMAT = '%b %d %Y %I:%M%p'

# Landing Page
def Home(request):
    return render(request,'home.html')
#Expected Json response endpoint view
def userAP(request):
    response_dict=dict()
    Members = User.objects.all()

    if(Members):
        response_dict['ok']='true'

        for user in Members:
            if ('members' not in response_dict):
                response_dict['members'] = list()

            response_dict['members'].append({
            	'id':user.user_id ,
                'real_name':user.real_name ,
                'tz':str(user.tz),
                'activity_periods':[
                    {
                    'start_time': datetime.strftime(period.start_time ,DATE_FORMAT),
                    'end_time' : datetime.strftime(period.end_time,DATE_FORMAT)
                    } for period in ActivityPeriod.objects.filter(User=user) ]
                    })

    else:
        response_dict['ok']='False'


    return JsonResponse(response_dict,json_dumps_params={'indent': 4},safe=False)

#using Api view creating json response
class userdata(APIView):
    def get(self,request):
        alluser= User.objects.all().values()
        allact = ActivityPeriod.objects.all().values()
        return Response({"ok":"true","members":alluser,"activity period": allact})

class  Userview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserSerializers

class  ActivityPeriodview(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class =  ActivityPeriodSerializers