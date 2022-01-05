from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = "Finally something together...just us"
    return HttpResponse(html)