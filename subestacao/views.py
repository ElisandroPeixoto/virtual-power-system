from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .equipamentos import Disjuntor

from django.http import HttpResponse


@login_required
def subestacao_simulacao(request):
    if request.method == "GET":
        correntes = {
            'mag_fasea': 0.00,
            'ang_fasea': 0.00,
            'mag_faseb': 0.00,
            'ang_faseb': 0.00,
            'mag_fasec': 0.00,
            'ang_fasec': 0.00,
            'mag_neutro': 0.00,
            'ang_neutro': 0.00
        }
        return render(request, 'subestacao_simu.html', correntes)
    else:
        al_1 = request.session['al_1']

        envios = {
            'al1_rele_50f': al_1
        }
        return render(request, 'subestacao_simu.html', envios)


@login_required
def al1(request):
    if request.method == "GET":
        return render(request, 'al1_simu.html')
    else:  # POST

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

        al_1 = Disjuntor(0, 0, 0, ifasea, ifaseb, ifasec)
        # *** ***

        pickup_50f = int(request.POST.get('prot50pp'))  # Relé 50 Fase
        al_1.rele_50f(pickup_50f)

        # Passando o objeto "AL-1" para outras views
        request.session['al_1'] = al_1.rele_50f(pickup_50f)

        correntes = {
            'mag_fasea': al_1.correntes[0][0],
            'ang_fasea': al_1.correntes[0][1],
            'mag_faseb': al_1.correntes[1][0],
            'ang_faseb': al_1.correntes[1][1],
            'mag_fasec': al_1.correntes[2][0],
            'ang_fasec': al_1.correntes[2][1],
            'mag_neutro': al_1.neutro()[0],
            'ang_neutro': al_1.neutro()[1],
        }

        return render(request, 'subestacao_simu.html', correntes)
