from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .calculo_medidas import calculo_neutro


@login_required
def subestacao_simulacao(request):
    return render(request, 'subestacao_simu.html')


@login_required
def al1(request):
    if request.method == "GET":
        return render(request, 'al1_simu.html')
    else:
        # *** Correntes ***
        # Fase A
        fasea_mag = int(request.POST.get('ia_magnitude'))
        fasea_ang = int(request.POST.get('ia_angulo'))
        ifasea = (fasea_mag, fasea_ang)

        # Fase B
        faseb_mag = int(request.POST.get('ib_magnitude'))
        faseb_ang = int(request.POST.get('ib_angulo'))
        ifaseb = (faseb_mag, faseb_ang)

        # Fase C
        fasec_mag = int(request.POST.get('ic_magnitude'))
        fasec_ang = int(request.POST.get('ic_angulo'))
        ifasec = (fasec_mag, fasec_ang)

        ig = calculo_neutro(ifasea, ifaseb, ifasec)

        return HttpResponse(f'{ig[0]} ∠ {ig[1]}')
