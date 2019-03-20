from django.shortcuts import redirect

def root_page(request):
    return redirect('/avengers/')
