from django.http import HttpResponse

# Create your views here.

from .models import Avenger

from django.shortcuts import render

def index(request):
    avenger_list = Avenger.objects.all()

    context = {
        'avenger_list': avenger_list,
    }

    return render(request, 'avengers/index.html', context)
    # return HttpResponse("You're in the avengers index")

def detail(request, avenger_name):
    response = "This is %s"
    return HttpResponse(response % avenger_name)

