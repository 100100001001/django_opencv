from . import views
from django.urls import path

from opencvapp.views import hehe

app_name = 'opencvapp'

urlpatterns = [
    path('start/', hehe, name='start'),
    path('detect', views.detectme, name="detect"),
    # path('calendar/', calendar, name='calendar'),
]