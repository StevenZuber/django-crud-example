from django.http import HttpResponse

# Create your views here.

from .models import Avenger

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.urls import reverse

from django.views import generic


class IndexView(generic.ListView):
    template_name = 'avengers/index.html'

    context_object_name = 'avenger_list'

    def get_queryset(self):
        return Avenger.objects.all()

class DetailView(generic.DetailView):
    model = Avenger

    template_name = 'avengers/detail.html'

class DeleteView(generic.DeleteView):
    model = Avenger

    template_name = 'avengers/index.html'


# def index(request):
#     avenger_list = Avenger.objects.all()
#
#     context = {
#         'avenger_list': avenger_list,
#     }
#
#     return render(request, 'avengers/index.html', context)
#
# def detail(request, avenger_name):
#
#     avenger = get_object_or_404(Avenger, avenger_name=avenger_name)
#
#     avenger.referrals += 1
#     avenger.save()
#
#     return render(request, 'avengers/detail.html', {'avenger': avenger})
#
# def delete(request, id):
#
#     avenger = get_object_or_404(Avenger, pk=id)
#
#     # if request.method == 'POST':
#     avenger.delete()
#
#     # avenger_list = Avenger.objects.all()
#     #
#     # context = {
#     #     'avenger_list': avenger_list,
#     # }
#
#     return HttpResponseRedirect(reverse(request, 'avengers/index.html'))
#     # return render(request, 'avenger/index.html', {'avenger': avenger})
