from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def selecao_simulacao(request):
    return render(request, 'menu_simu.html')
