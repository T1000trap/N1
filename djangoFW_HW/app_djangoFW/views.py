from django.shortcuts import render
from .models import Advertisment
from django.http import HttpResponse


def index(request):
    advertisments =  Advertisment.objects.all()
    context = {"advertisments" : advertisments}
    return render(request, "index.html", context)

def top_sellers(requests):
    return render(requests, "top-sellers.html")