from .calculo_medidas import calculo_neutro


class Equipamento:
    def __init__(self, tensao_va, tensao_vb, tensao_vc, corrente_ia, corrente_ib, corrente_ic):
        self.__tensao_va = tensao_va
        self.__tensao_vb = tensao_vb
        self.__tensao_vc = tensao_vc
        self.__corrente_ia = corrente_ia
        self.__corrente_ib = corrente_ib
        self.__corrente_ic = corrente_ic
        self.__corrente_ig = 0

    @property
    def tensoes(self):
        return self.__tensao_va, self.__tensao_vb, self.__tensao_vc

    @property
    def correntes(self):
        return self.__corrente_ia, self.__corrente_ib, self.__corrente_ic

    def neutro(self):
        self.__corrente_ig = calculo_neutro(self.__corrente_ia, self.__corrente_ib, self.__corrente_ic)
        return self.__corrente_ig


class Disjuntor(Equipamento):
    def __init__(self, tensao_va, tensao_vb, tensao_vc, corrente_ia, corrente_ib, corrente_ic):
        super().__init__(tensao_va, tensao_vb, tensao_vc, corrente_ia, corrente_ib, corrente_ic)

        self.__status = False

    def rele_50f(self, pickup_50):  # >>> FALTA CORRIGIR ESSA LÓGICA DO RELÉ <<<
        if (self.correntes[0][0] or self.correntes[1][0] or self.correntes[2][0]) > pickup_50:
            return 'Atuação 50 Fase'
        else:
            return 'Tudo Normal'
