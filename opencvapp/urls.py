from django.urls import path

from opencvapp.views import hehe

app_name = 'opencvapp'

urlpatterns = [
    path('start/', hehe, name='start'),
]