from django.http import HttpResponse

# Create your views here.

from .models import Avenger

def index(request):
    avenger_list = Avenger.objects.all()

    output = ', '.join([avenger.avenger_name for avenger in avenger_list])
    return HttpResponse(output)
    # return HttpResponse("You're in the avengers index")

def detail(request, avenger_name):
    return HttpResponse("This is %s" % avenger_name)

