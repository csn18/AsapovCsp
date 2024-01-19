from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Main.models import Performance


def cadets_list(request):
    cadets = User.objects.filter(is_staff=False)
    return render(request, 'cadets.html', locals())


def cadet_detail(request, pk):
    cadet = User.objects.get(id=pk)
    perfomances = Performance.objects.filter(cadet=cadet)
    return render(request, 'cadet.html', locals())


def handler_404(request, exception):
    return redirect('cadets_list')
