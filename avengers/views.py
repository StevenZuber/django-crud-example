from .models import Avenger
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AvengerForm


def index(request):

    if request.method == 'GET':
        avenger_list = Avenger.objects.all()

        context = {
            'avenger_list': avenger_list,
        }
    if request.method == 'POST':
        form = AvengerForm(request.POST)

        if form.is_valid():
            avenger = form.save(commit=False)
            avenger.save()

            avenger_list = Avenger.objects.all()
            context = {
                'avenger_list': avenger_list,
            }

            return render(request, 'avengers/index.html', context)

    else:
        avenger_list = Avenger.objects.all()

        context = {
            'avenger_list': avenger_list,
        }
        return render(request, 'avengers/index.html', context)

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
        avenger_list = Avenger.objects.all()

        context = {
            'avenger_list': avenger_list,
        }
        return render(request, 'avengers/index.html', context)

    avenger_list = Avenger.objects.all()

    context = {
        'avenger_list': avenger_list,
    }
    return render(request, 'avengers/index.html', context)


def update(request, id):
    return"temp"


# def create(request):
#
#     if request.method == 'POST':
#         form = AvengerForm(request.POST)
#
#         if form.is_valid():
#             avenger = form.save(commit=False)
#             avenger.save()
#             # avenger_list = Avenger.objects.all()
#             #
#             # context = {
#             #     'avenger_list': avenger_list,
#             # }
#             return redirect('avengers/detail.html', {'avenger': avenger})
#
#     else:
#         avenger_list = Avenger.objects.all()
#
#         context = {
#             'avenger_list': avenger_list,
#         }
#         return render(request, 'avengers/index.html', context)


# class IndexView(generic.ListView):
#     template_name = 'avengers/index.html'
#
#     context_object_name = 'avenger_list'
#
#     def get_queryset(self):
#         return Avenger.objects.all()
#
# class DetailView(generic.DetailView):
#     model = Avenger
#
#     template_name = 'avengers/detail.html'
#
# class DeleteView(generic.DeleteView):
#     model = Avenger
#
#     template_name = 'avengers/index.html'
#
