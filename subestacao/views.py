from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


@login_required
def subestacao_simulacao(request):
    return render(request, 'subestacao_simu.html')


@login_required
def al1(request):
    if request.method == "GET":
        return render(request, 'al1_simu.html')
    else:
        prot50pp = request.POST.get('prot50pp')
        nome = str(prot50pp)
        return HttpResponse(nome)
