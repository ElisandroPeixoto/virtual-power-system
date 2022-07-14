from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def subestacao_simulacao(request):
    return render(request, 'subestacao_simu.html')
