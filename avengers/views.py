from django.http import HttpResponse

# Create your views here.

from .models import Avenger

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.urls import reverse

def index(request):
    avenger_list = Avenger.objects.all()

    context = {
        'avenger_list': avenger_list,
    }

    return render(request, 'avengers/index.html', context)
    # return HttpResponse("You're in the avengers index")

def detail(request, avenger_name):

    avenger = get_object_or_404(Avenger, avenger_name=avenger_name)

    avenger.referrals += 1
    avenger.save()

    return render(request, 'avengers/detail.html', {'avenger': avenger})
