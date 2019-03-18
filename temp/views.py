from django.http import HttpResponse

def root_page(request):
    return HttpResponse("Welcome to the Root Homepage!")
