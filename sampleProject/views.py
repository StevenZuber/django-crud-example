from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")

def root_page(request):
    return HttpResponse("Welcome to the Root Homepage!")