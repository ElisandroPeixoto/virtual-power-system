import cmath, math
import numpy as np


ia_mag = 86.60
ia_ang = -50j

ib_mag = -86.60
ib_ang = -50j

ic_mag = 0
ic_ang = 100j


ia = ia_mag + ia_ang
ib = ib_mag + ib_ang
ic = ic_mag + ic_ang


def corrente_neutro(i_fasea, i_faseb, i_fasec):
    ig = i_fasea + i_faseb + i_fasec
    return ig


neutro = corrente_neutro(ia, ib, ic)

print(neutro)
print(cmath.polar(neutro))

""" ARQUIVO EM CONSTRUÇÃO """
