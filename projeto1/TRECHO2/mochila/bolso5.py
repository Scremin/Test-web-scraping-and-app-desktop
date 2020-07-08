# bolso 5. Organização final.
import pandas as pd

def V_op1(x, y, z, w):
    '''
       Retornar a informação equivalente aos dados do scraping e
       suas interrelações. Engloba V1, V2, V3, V4 e V5, pois possuem características
       semelhantes para as operações nessa função.
    '''
    # x = valor anterior. y = previsão. z = nome do evento.
    li = list()
    delta = abs(y-x) # Diferença de valor.
    opX = abs(x) # Valor anterior é a referência, nesse caso de cálculo.
    porc = int((delta*100)/opX)
    if x < y:
        var = f'Evento: {z}'
        li.append(var)
        var = f'Previsão: {porc}% de alta em relação ao valor anterior.'
        li.append(var)
        var = w # hora.
        li.append(var)
    elif x == y:
        var = f'Evento: {z}'
        li.append(var)
        var = f'Previsão de manutensão do valor anterior.'
        li.append(var)
        var = w
        li.append(var)
    else: # x < y
        var = f'Evento: {z}'
        li.append(var)
        var = f'Previsão: {porc}% de baixa em relação ao valor anteiror.'
        li.append(var)
        var = w
        li.append(var)
    return li


def V_op2(ant, nome, w): # valor anterior e o nome.
    '''
        Engloba apenas a referência V6: Evento sem previsão.
    '''
    li = list()
    var = f'Evento: {nome}'
    li.append(var)
    var = f'Previsão: Sem previsão para este evento.'
    li.append(var)
    var = w # hora.
    li.append(var)
    return li


def V_op3(x, y, z, w):
    '''
        Engloba as referências de V7 à V14.
    '''
    li = list()
    delta = abs(y-x) # Diferença de valor.
    opX = abs(x)
    porc = int((delta*100)/opX)
    if x < y:
        var = f'Evento: {z}'
        li.append(var)
        var = f'Previsão: {porc}% de alta em relação ao valor anterior.'
        li.append(var)
        var = w # hora.
        li.append(var)
    elif x == y:
        var = f'Evento: {z}'
        li.append(var)
        var = f'Previsão de manutensão do valor anterior.'
        li.append(var)
        var = w
        li.append(var)
    else: # x < y
        var = f'Evento: {z}'
        li.append(var)
        var = f'Previsão: {porc}% de baixa em relação ao valor anteiror.'
        li.append(var)
        var = w
        li.append(var)
    return li


def V_op4(nome):
    '''
        Evento sem informação numérica.
    '''
    li = list()
    var = f'Evento: {nome}'
    li.append(var)
    var = f'Previsão: Não há informação numérica sobre este evento.'
    li.append(var)
    return var


def L_BPS2(arg, z):
    '''
        Retorna x: uma lista com a informação relativa ao acontecimento (evento).
    '''
    # De V1 à V5.
    if arg == 1 or arg == 2 or arg == 3 or arg == 4 or arg == 5:
        # V_op1(valor anterior = x, previsão = y, nome).
        x = V_op1(z[-2], z[-1], z[-3], z[-4]) # BPS2[c][-2], BPS2[c][-1], BPS2[c][-3].
        return x
    # V6.
    elif arg == 6: # Deve indicar que não há previsão de resultado para o evento.
        x = V_op2(z[-1], z[-3], z[-4]) # valor anterior, nome, hora.
        return x
    # De V7 à V14.
    elif arg >= 7 and arg <= 14:
        x = V_op3(z[-2], z[-1], z[-4], z[-5])
        return x
    elif arg == 15:
        x = V_op4(z[-1]) # Não há INFO, apenas o nome para o identificar.
        return x
    else:
        return 0


def L_BPS1(elem, nome):
    '''
        Retorna x: uma lista com a informação relativa ao acontecimento (evento).
    '''
    #
    elemAnt = elem[-2] # valor anterior.
    elemPrev = elem[-1] # previsão.
    hora = elem[0]
    if elemPrev == '—':
        elemAnt = float(elemAnt) # Converter para float antes de operar.
        x = V_op2(elemAnt, nome, hora) # valor anterior, nome.
        return x
    else:
        elemAnt = float(elemAnt) # Converter para float antes de operar.
        try:
            elemPrev = float(elemPrev) # Converter para float antes de operar.
        except:
            # CARACTERISTICA DA INFO NO SITE 1.
            # pode ser uma str e não um número.
            # Nesse caso, o valor anterior está na posição da previsão.
            # exemplo: [12, 'Goods Trade Balance (R)', ' B', '-70.73', 'B']
            elemPrev = elemAnt # SERÃO IGUAIS, NESSE CASO.
        #
        x = V_op1(elemAnt, elemPrev, nome, hora) #
        return x
    return 0


def preFinal(BPS2, BPS1):
    #
    # TESTE DE VERIFICAÇÃO DE PROPAGAÇÃO DE ERROR.
    if BPS1 == 0:
        # Então utilizar apenas a BPS2.
        Li_aux_s2 = list()
        c = 0
        while c < len(BPS2):
            arg_aux = BPS2[c][0]
            arg = (int(arg_aux[-2:])) # elem referência V, conv para inteiro.
            res = L_BPS2(arg, BPS2[c]) # referência e o elemento.
            Li_aux_s2.append(res)
            c += 1
        c = 0
        INFO_END = [Li_aux_s2, 0]
        novodic = pd.DataFrame({'ListaFront': INFO_END})
        novodic.to_pickle('tmpSaveFrontEnd.pk1') # Save.
        return INFO_END
    #
    else:
        Li_aux_s2 = list()
        Li_aux_s1 = list()
        c = 0
        while c < len(BPS2):
            arg_aux = BPS2[c][0]
            arg = (int(arg_aux[-2:])) # elem referência V, conv para inteiro.
            res = L_BPS2(arg, BPS2[c]) # referência e o elemento.
            Li_aux_s2.append(res)
            c += 1
        c = 0
        while c < len(BPS1):
            #
            res = L_BPS1(BPS1[c], BPS1[c][1]) # elemento e o nome do elemento (evento).
            Li_aux_s1.append(res)
            c += 1
        INFO_END = [Li_aux_s2, Li_aux_s1]
        novodic = pd.DataFrame({'ListaFront': INFO_END})
        novodic.to_pickle('tmpSaveFrontEnd.pk1') # Save.
        #novo_b = pd.read_pickle('tmpSaveFrontEnd.pk1') # Confirmação do save.

        return INFO_END # Retorna 2 listas de listas finalmento processadas.
    return 0 # ERROR.
