import cmath
import numpy as np


def retangular(vi_fasepolar):
    """Converte um complexo polar para retangular"""
    valor_rect = cmath.rect(vi_fasepolar[0], np.deg2rad(vi_fasepolar[1]))
    return valor_rect


def polar(vi_faserect):
    """Converte um complexo em retangular para polar"""
    valor_polar_rad = cmath.polar(vi_faserect)
    valor_polar_deg = round(valor_polar_rad[0], 2), round((np.rad2deg(valor_polar_rad[1])), 2)
    return valor_polar_deg


def calculo_neutro(ifasea, ifaseb, ifasec):
    """Calcula a corrente de neutro de um sistema trifásico Y"""
    iarec = retangular(ifasea)
    ibrec = retangular(ifaseb)
    icrec = retangular(ifasec)

    igrec = iarec + ibrec + icrec

    igpol = polar(igrec)
    return igpol
