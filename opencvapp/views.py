from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hehe(request):
    return render(request, 'opencvapp/index.html')