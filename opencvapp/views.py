from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hehe(request):
    return HttpResponse('안녕하세요! 시작해보겠습니다!')