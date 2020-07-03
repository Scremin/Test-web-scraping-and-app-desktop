from mochila.bolso1 import capt, decS1, decS2, separS2
from mochila.bolso2 import ajusteIntPreOp, ajustoHora, ajusteNovaLista, rel

def capt(s_url, s_IDbuscado):
    '''
        Recolhe as informações localizadas numa posição específica
        de cada endereço.
    '''
    s = capt(s_url, s_IDbuscado)
    return s


def dec(s1, s2):
    '''
        As strings recebidas são recortadas de acordo
        com as características do site e das informações relevantes.
        São retornados dois dicionários com a primeira posição preenchida
        com uma lista de listas.
    '''
    dic_s1 = decS1(s1)
    #
    li_s2_temp = decS2(s2)
    dic_s2 = separS2(li_s2_temp)
    #
    return dic_s1, dic_s2


def ajuste(dic_s1, dic_s2):
    '''
        Preparação do relacionamento.
    '''
    li_int = ajusteIntPreOp(dic_s1)
    li_temp = ajustoHora(li_int)
    liS1 = ajusteNovaLista(li_temp, li_int)
    #
    liS2 = ajusteIntPreOp(dic_s2)
    #
    return liS1, liS2


def relacio(liS2, liS1):
    '''
         RELACIONAMENTO s1 <-> s2.
         Desta etapa é retornada uma lista, ou com os matching ou com uma flag=0,
         correspondendo à utilização da lista s2, filtrada por EURUSD,
         para ter seus componentes analisados isoladamente, sem utilizar s1.
    '''
    nLi, flag = rel(liS2, liS1) # (lista referência, lista analisada).
    # Se a flag indicar que não houve matching, então usa a lista s2 filtrada por EURUSD.
    if flag == 0:
        flag = 0
        return liS2, flag # Retorna a lista s2 e o indicador de error.
    else:
        return nLi, flag # Retorna a lista matching e sua quantidade de elementos
    return [-1], -1 # Retorna -1 indicando error.
