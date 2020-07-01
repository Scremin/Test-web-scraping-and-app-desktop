from mochila.bolso1 import capturador, decepamentoS1, decepamentoS2, separS2

def captura(s_url, s_IDbuscado):
    s = capturador(s_url, s_IDbuscado)
    return s


def decepamento(s1, s2):
    '''
        Decepamento.
    '''
    dic_s1 = decepamentoS1(s1)
    #
    li_s2_temp = decepamentoS2(s2)
    dic_s2 = separS2(li_s2_temp)
    #
    return dic_s1, dic_s2
