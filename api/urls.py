from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.Userview)
router.register('ActivityPeriod',views.ActivityPeriodview)

urlpatterns = [
    path('', views.Home, name ='home'),
    path('userAP/',views.userAP, name='userAP'),
    path('userdata/',views.userdata.as_view(), name='userdata'),
    path('api/', include(router.urls),name='api'),

]