from .models import Avenger
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AvengerForm


def index(request):

    # allows user to add to the roster without having to load a separate page
    if request.method == 'POST':
        form = AvengerForm(request.POST)

        if form.is_valid():
            avenger = form.save(commit=False)
            avenger.save()

            avenger_list = Avenger.objects.all()
            new_context = {
                'avenger_list': avenger_list,
            }

            return render(request, 'avengers/index.html', new_context)

    else:
        avenger_list = Avenger.objects.all()

        context = {
            'avenger_list': avenger_list,
        }
        return render(request, 'avengers/index.html', context)


def detail(request, avenger_name):

    avenger = get_object_or_404(Avenger, avenger_name=avenger_name)

    avenger.referrals += 1
    avenger.save()

    return render(request, 'avengers/detail.html', {'avenger': avenger})


def delete(request, id):
    avenger = get_object_or_404(Avenger, id=id)

    if request.method == 'POST':
        avenger.delete()

        return redirect('/avengers/')

    avenger_list = Avenger.objects.all()

    context = {
        'avenger_list': avenger_list,
    }
    return render(request, 'avengers/index.html', context)


def update(request, id):
    avenger = get_object_or_404(Avenger, id=id)
    if request.method == "POST":
        form = AvengerForm(request.POST, instance=avenger)
        if form.is_valid():
            avenger = form.save(commit=False)
            avenger.save()

            return redirect('/avengers/')
    else:
        return redirect('/avengers/')
