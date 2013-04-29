# Create your views here.

from django.http import HttpResponse
from example_app.models import Poll
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world . You are in example_app index")


def details(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return render(request,'example_app/detail.html',{'poll':poll}) 
