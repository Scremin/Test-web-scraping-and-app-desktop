# BOLSO 4. BPS1. Lista final: [hora, nome, excedente, carac, anterior, previsão].

def compAUX(carac, sinal, lastCarac):
    '''
        Função que itera comparando o caractere recebido com uma lista de
        caracteres definidos.
        Retorna o nº de iterações.
    '''
    #print('entrada na func compIntAUX')
    if sinal == 'a': # ROT1
        LiInt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LiInt2 = ['—', 'M', '%', '$'] # '—', , ')'
    elif sinal == 'b': # ROT3
        LiInt = ['M', '%', '$']
        LiInt2 = ['—'] # alfa.
    elif sinal == 'c': # ROT 2.
        LiInt = [lastCarac]
        LiInt2 = ['—', '$'] # alfa.
    elif sinal == 'd': # ROT 4.
        LiInt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LiInt2 = ['—', '$'] # alfa.
    else:
        print('ERROR NO SINAL DE REFERÊNCIA (BPS1)')
    i = 0
    j = 0
    while i == 0:
        while j < len(LiInt):
            if carac == LiInt[j]: # Se o carac for um nº, um esp, ou o last. Dependendo do sinal.
                return 1
            else:
                k = 0
                while k < len(LiInt2):
                    if carac == LiInt2[k]: # Se o carac for um esp ou alfa. Dependendo do sinal.
                        return 2
                    else:
                        pass
                    k += 1
            j = j + 1
        i += 1
        return 0


def rot(STR_INFO, sinal, lastCarac):
    '''
        Condições baseados no 1º tipo de caractere encontrado. Podendo ser
        um especial, um número ou o elemento alfa. Ainda que, existem as
        opções de serem encontrados ou na 1ª iteração de busca ou não.
        Retorna o tamanho do corte necessário.
    '''
    #
    i = 1
    j = 1
    while i == 1:
        while j <= (len(STR_INFO)):
            num = j
            comp1 = compAUX(STR_INFO[-num], sinal, lastCarac) # Valor do evento anterior.
            if comp1 == 0: # se não for um número.
                pass
            elif comp1 == 1: # Se for um nº, sem carac especial.
                if j != 1: # Para evitar um corte = 0, caso estêjamos na 1ª iteração.
                    num = j - 1
                    # rot2.
                    return num
                else:
                    num = j
                    return num
            elif comp1 == 2: # Se for um caractere especial.
                if j != 1: # Para um corte = 0, caso estêjamos na 1ª iteração.
                    num = j - 1
                    # rot2.
                    return num
                else:
                    num = j
                    # rot3.
                    return num
                return 2
            j += 1
        i += 1
    return 0


def BPS1(s1):
    '''
        Recebimento da str s1 e o respectivo corte relacionado ao
        conteúdo presente na componente INFO.
        Retorna uma lista de listas com o processamento s1 concluído.
    '''
    # TESTE DE VERIFICAÇÃO DE PROPAGAÇÃO DE ERROR.
    if s1[0][3] == 0: # Se a posição especificada for zero.
        # Então indica que s1 possui a lista ERROR: [[0, 0, 0, 0]].
        return 0 # Fim da rotina BPS1, fim do bolso4.
    
    tam = len(s1)
    liFinal = list()
    q = 0
    while q < tam:
        li_cont = list()
        
        STR_HORA = s1[q][0] # Hora do elemento.
        li_cont.append(STR_HORA)
        STR_NOME = s1[q][2] # Nome do elemento.
        li_cont.append(STR_NOME)
        
        STR_INFO = s1[q][1]
        #print(STR_INFO)
        #  rot 1 == a.
        num = rot(STR_INFO, 'a', '') # RETORNA O Nº DE CORTE.

        novaStr1 = STR_INFO[:-num]
        var = len(STR_INFO)-num
        parte1 = STR_INFO[var:]
        li_cont.append(parte1)
        if num != 1:
            posiTeste = novaStr1[-1]
            aux = compAUX(posiTeste, 'a', '')
            if aux == 1:
                # NÃO HÁ CARACTERE ESPECIAL ACOMPANHANDO O NÚMERO.
                #
                lastCarac = STR_INFO[-1]

                #  rot 2.
                num = rot(novaStr1, 'c', lastCarac) # RETORNA O Nº DE CORTE. ROT 2 = c.
                novaStr2 = novaStr1[:-num]
                var = len(novaStr1)-num
                parte2 = novaStr1[var:]
                li_cont.append(parte2)

                #  rot 4.
                num = rot(novaStr2, 'd', lastCarac) # RETORNA O Nº DE CORTE. ROT 4 = d.
                novaStr3 = novaStr2[:-num]
                var = len(novaStr2)-num
                parte3 = novaStr2[var:]
                #li_cont.append(parte3)

                #  rot 2.
                num = rot(novaStr3, 'c', lastCarac) # RETORNA O Nº DE CORTE. ROT 2 = c.
                novaStr4 = novaStr3[:-num]
                var = len(novaStr3)-num
                parte4 = novaStr3[var:]
                li_cont.append(parte4)

                if len(novaStr4) <= 2:
                    print(f'INFO s1 [{q}] verificada com sucesso.')
                else:
                    print(f'Tamanho da INFO [{q}] fora do padrão.') 
            elif aux == 2:
                # CARACTERE ESPECIAL ENCONTRADO 1º QUE O NÚMERO.
                # rot 2.
                lastCarac = STR_INFO[-1]
                #print(lastCarac)

                # rot 1 == a.
                num = rot(novaStr1, 'a', lastCarac) # RETORNA O Nº DE CORTE.
                novaStr2 = novaStr1[:-num]
                var = len(novaStr1)-num
                parte2 = novaStr1[var:]
                li_cont.append(parte2)

                #  rot 2 == c.
                num = rot(novaStr2, 'c', lastCarac) # RETORNA O Nº DE CORTE.
                novaStr3 = novaStr2[:-num]
                var = len(novaStr2)-num
                parte3 = novaStr2[var:]
                li_cont.append(parte3)

                #  rot 4 == d.
                num = rot(novaStr3, 'd', lastCarac) # RETORNA O Nº DE CORTE.
                novaStr4 = novaStr3[:-num]
                var = len(novaStr3)-num
                parte4 = novaStr3[var:]
                #li_cont.append(parte4)

                # rot 2.
                num = rot(novaStr4, 'c', lastCarac) # RETORNA O Nº DE CORTE.
                novaStr5 = novaStr4[:-num]
                var = len(novaStr4)-num
                parte5 = novaStr4[var:]
                li_cont.append(parte5)

                if len(novaStr5) <= 2:
                    print(f'INFO s1 [{q}] verificada com sucesso.')
                else:
                    print(f'Tamanho da INFO [{q}] s1 fora do padrão.')    
        else:
            # rot 3 == b.
            num = rot(novaStr1, 'b', '') # RETORNA O Nº DE CORTE. ROT 3 = b.
            novaStr2 = novaStr1[:-num]
            var = len(novaStr1)-num
            parte2 = novaStr1[var:]
            li_cont.append(parte2)

            # rot 3.
            num = rot(novaStr2, 'b', '') # RETORNA O Nº DE CORTE. ROT 3 = b.
            novaStr3 = novaStr2[:-num]
            var = len(novaStr2)-num
            parte3 = novaStr2[var:]

            # rot 3.
            num = rot(novaStr3, 'b', '') # RETORNA O Nº DE CORTE. ROT 3 = b.
            novaStr4 = novaStr3[:-num]
            var = len(novaStr3)-num
            parte4 = novaStr3[var:]
            li_cont.append(parte4)

            if len(novaStr4) <= 2:
                print(f'INFO s1 [{q}] verificada com sucesso.')
            else:
                print(f'Tamanho da INFO [{q}] s1 fora do padrão.')
        liFinal.append(li_cont)
        q += 1
    return liFinal # retorna BPS1.

