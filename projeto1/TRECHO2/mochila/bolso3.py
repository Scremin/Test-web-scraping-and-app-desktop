# BOLSO 3: processamento da informação do site 2: referência.

def compIntAUX(carac):
    '''
        Função que itera comparando o caractere recebido com uma lista de
        inteiros. Objtivando varrer a string recebida, caractere à caractere.
        Retornar 1 Se encontrar um número.
    '''
    LiInt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 0
    var1 = 0
    var2 = 0
    j = 0
    while i == 0:
        while j < len(LiInt):
            if carac == LiInt[j]: # Se o caractere for um número da lista.
                return 1
            else:
                pass
            j = j + 1
        i += 1
        return 0


def compInt(carac):
    '''
        Função que itera comparando o caractere recebido com uma lista de
        inteiros. Objetivando encontrar qual o número inteiro recebido com parâmetro.
    '''
    LiInt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 0
    while i < len(LiInt):
        if carac == LiInt[i]: # Se o caractere for um número da lista.
            retorno = True
        else:
            retorno = False
        if retorno == True:
            return retorno
        i = i + 1
        

def compEsp(carac):
    '''
        Função que itera comparando o caractere recebido com uma lista de
        caracteres especiais.
    '''
    LiEsp = ['%', 'M']
    i = 0
    while i < len(LiEsp):
        if carac == LiEsp[i]: # Se o caractere for um caractere especial.
            retorno = True
        else:
            retorno = False
        if retorno == True:
            return retorno
        i = i + 1


def tamanhinho1(tamanY, y):
    '''
        Recebe o tamanho da str com o último caractere, especial.
        Com o objetivo de encontrar o tamanho numérico e separadamente.
        Retorna o tamanho do número.
    '''
    # PARCIAL À Y.
    i = 1 # -1 == -L == último. (!). Reverificação do último devido ao tamanho final gerado.
    L = 0 # contador.
    j = 1
    while i == 1:
        while j < tamanY:
            # Contagem decrescente.
            num = j
            comp1 = compIntAUX(y[-num]) # Valor do evento anterior.
            if comp1 == 0: # se não for um número.
                pass
            elif comp1 == 1: # Se nº.
                nTamanY = tamanY - j + 1 # +1 devido à j começar em 1.
                return nTamanY
            j += 1
        i = i + 1
        # Se o loop acabar sem número nenhum.
        print('Não há previsão numérica para este evento s2.')
        return -1 # retorno de error.


def tamanhinho2(tamanX, x):
    '''
        Recebe o tamanho da str com o último caractere, especial.
        Com o objetivo de encontrar o tamanho numérico e separadamente.
        Retorna o tamanho do número.
    '''
    # PARCIAL À X.
    L = 1 # -1 == -L == último. (!). Reverificação do último devido ao tamanho final gerado.
    j = 1
    i = 1
    while i == 1:
        while j < tamanX:
            # Contagem decrescente.
            num = j
            comp1 = compIntAUX(x[-num]) # Valor da previsão do evento.
            if comp1 == 0: # se não for um número.
                L =  L + 1
            elif comp1 == 1: # Se nº.
                nTamanX = tamanX - j + 1 # +1 devido à j começar em 1.
                return nTamanX
            j += 1
        i = i + 1
        # Se o loop acabar sem número nenhum.
        print('Não há previsão numérica para este evento s2.')
        return -1 # retorno de error.


def BPS2(Li):
    '''
        Li é a lista a ter seus elementos de informação analisado.
        Essa lista pode ser ou uma lista de matching ou
        apenas a lista s2 filtrada por EURUSD.
    '''
    c = 0
    listaE = list()
    t = len(Li)
    #
    while c < t: 
        elem = Li[c] # COMPARAÇÃO DO ÚLTIMO CARACTERE.
        carac = elem[-1][-1] # Último caractere da última str.
        num = compInt(carac)
        num2 = compEsp(carac)
        if num is True: # Se o último caractere for um número.
            tamX = len(elem[-1])
            x = (elem[-1]) # receber a previsão. str.
            num = compInt(elem[-2][-1]) # Último caractere da penúltima str.
            if num is True: # Se o último caractere da penúltima str for um número.
                tamY = len(elem[-2])
                y = (elem[-2]) # receber o (valor anterior)(evento). str.
                horaEvento = elem[0]
                nomeEvento = elem[2] # Primeira parte do nome.
                listaB = list()
                j = 3 # A partir do índice que inicia o nome + 1.
                while j < (len(elem)-2): # receber o nome completo do evento.
                    nomeEvento = nomeEvento + elem[j] + ' ' # Soma de strings.
                    j += 1
                # Verificação de tamanho e especificidades de sinais.
                if tamX == tamY:
                    # Então os dois números têm o mesmo tamanho.
                    # A lista recebe a referência V1.
                    # z será o novo resultado.
                    x = (float(elem[-1]))
                    y = (float(elem[-2]))
                    listaA = ['V01', tamX, horaEvento, nomeEvento, x, y]
                else:
                    # Se não, se os tam forem !=, verificar o 1º caractere das 2 strings.
                    if x[0] == '-' and y[0] == '-': # Se ambas forem nº negativo.
                        # Então os dois números são negativos com tamanhos diferentes.
                        x = (float(elem[-1])) # receber a conversão para inteiro da previsão.
                        y = (float(elem[-2])) # Converte o (valor anterior)(evento) para inteiro.
                        listaA = ['V02', tamX, tamY, horaEvento, nomeEvento, x, y]
                    elif x[0] == '-' and y[0] != '-':
                        # Então apenas a previsão é negativa.
                        x = (float(elem[-1])) # receber a conversão para inteiro da previsão.
                        y = (float(elem[-2])) # Converte o (valor anterior)(evento) para inteiro.
                        listaA = ['V03', tamX, tamY, horaEvento, nomeEvento, x, y]
                    elif x[0] != '-' and y[0] == '-':
                        # Então apenas o valor anteior é negativo.
                        x = (float(elem[-1])) # receber a conversão para inteiro da previsão.
                        y = (float(elem[-2])) # Converte o (valor anterior)(evento) para inteiro.
                        listaA = ['V04', tamX, tamY, horaEvento, nomeEvento, x, y]
                    elif x[0] != '-' and y[0] != '-':
                        # Então os 2 nº são POSITIVOS, de tamanho diferente.
                        if tamX > tamY:
                            tamY +=1
                        elif tamX < tamY:
                            tamX +=1
                        x = (float(elem[-1])) # receber a conversão para inteiro da previsão.
                        y = (float(elem[-2])) # Converte o (valor anterior)(evento) para inteiro.
                        listaA = ['V05', tamX, tamY, horaEvento, nomeEvento, x, y]
                #listaB.append(listaA)
                listaE.append(listaA)
        # Se não, se o caractere não for um número, mas sim um caractere especial.
        elif num2 is True: # Último caractere da última str.
            carac = elem[-1][-2]
            num = compInt(carac)
            if num is True: # Se o penúltimo caractere da última str for um número.
                # Se o último caractere das 2 últimas str forem iguais.
                if elem[-2][-1] == elem[-1][-1]:
                    carac = elem[-1][-1] # caractere especial.
                    x = (elem[-1]) # receber str previsão. Com o caractere especial.
                    tamanX = len(x)
                    y = (elem[-2]) # receber str V. anterior. Com o caractere especial.
                    tamanY = len(y)
                    horaEvento = elem[0]
                    nomeEvento = elem[2] # Primeira parte do nome.
                    listaD = list()
                    j = 3 # A partir do índice que inicia o nome + 1.
                    while j < len(elem)-2: # receber o nome completo do evento.
                        nomeEvento = nomeEvento + elem[j] + ' ' # Soma de strings.
                        j += 1
                    tamanY = tamanhinho1(tamanY, y)
                    tamanX = tamanhinho2(tamanX, x)
                    if tamanX != -1: # Se o resultado de tamanhinho não for errôneo.
                        if tamanX == tamanY: # Se forem iguais.
                            if x[0] == '-' and y[0] == '-': # Se ambas forem nº negativo.
                                # Então os dois números são negativos com tamanhos iguais.
                                y = (float(elem[-2][0:-1]))
                                x = (float(elem[-1][0:-1])) # receber float previsão. Sem o carac
                                listaC = ['V07', tamanX, tamanY, horaEvento, nomeEvento, carac, x, y]
                                listaE.append(listaC)
                            elif x[0] == '-' and y[0] != '-':
                                # Então apenas a previsão é negativa.
                                y = (float(elem[-2][0:-1]))
                                x = (float(elem[-1][0:-1])) # receber float previsão. Sem o carac
                                listaC = ['V08', tamanX, tamanY, horaEvento, nomeEvento, carac, x, y]
                                listaE.append(listaC)
                            elif x[0] != '-' and y[0] == '-':
                                # Então apenas o valor anteior é negativo.
                                y = (float(elem[-2][0:-1]))
                                x = (float(elem[-1][0:-1]))
                                listaC = ['V09', tamanX, tamanY, horaEvento, nomeEvento, carac, x, y]
                                listaE.append(listaC)
                            elif x[0] != '-' and y[0] != '-':
                                # Então os 2 nº são positivos, de tamanho iguais.
                                y = (float(elem[-2][0:-1]))
                                x = (float(elem[-1][0:-1]))
                                listaC = ['V10', tamanX, tamanY, horaEvento, nomeEvento, carac, x, y]
                                listaE.append(listaC)
                        else: # Se os tamanhos forem diferentes.
                            # Então verificar o 1º caractere.
                            if x[0] == '-' and y[0] == '-': # Se ambas forem nº negativo.
                                # Então os dois números são negativos com tamanhos diferentes.
                                y = (float(elem[-2][0:-1]))
                                x = (float(elem[-1][0:-1]))
                                listaC = ['V11', tamanX, tamanY, horaEvento, nomeEvento, carac, x, y]
                                listaE.append(listaC)
                            elif x[0] == '-' and y[0] != '-':
                                # Então apenas a previsão é negativa.
                                y = (float(elem[-2][0:-1]))
                                x = (float(elem[-1][0:-1]))
                                listaC = ['V12', tamanX, tamanY, horaEvento, nomeEvento, carac, x, y]
                                listaE.append(listaC)
                            elif x[0] != '-' and y[0] == '-':
                                # Então apenas o valor anteior é negativo.
                                y = (float(elem[-2][0:-1]))
                                x = (float(elem[-1][0:-1]))
                                listaC = ['V13', tamanX, tamanY, horaEvento, nomeEvento, carac, x, y]
                                listaE.append(listaC)
                            elif x[0] != '-' and y[0] != '-':
                                # Então os 2 nº são positivos, de tamanho diferente.
                                y = (float(elem[-2][0:-1]))
                                x = (float(elem[-1][0:-1]))
                                listaC = ['V14', tamanX, tamanY, horaEvento, nomeEvento, carac, x, y]
                                listaE.append(listaC)
                    else: # Se foi não houve resultado numérico.
                        # Então não há previsão para este evento.
                        listaC = ['V15', nomeEvento]
                        listaE.append(listaC)
                else: # Se o último caractere das 2 últimas str forem diferentes.
                    # Então não há previsão.
                    carac = elem[-1][-1] # caractere especial.
                    horaEvento = elem[0]
                    nomeEvento = elem[2] # Primeira parte do nome.
                    listaD = list()
                    j = 3 # A partir do índice que inicia o nome + 1.
                    while j < len(elem)-1: # receber o nome completo do evento. (-1 componente: última str)
                        nomeEvento = nomeEvento + elem[j] + ' ' # Soma de strings.
                        j += 1
                    x = (float(elem[-1][0:-1])) # receber float do valor anterior. Sem o caractere especial.
                    #listaC = ['V6', tamanX, horaEvento, nomeEvento, carac, x]
                    listaC = ['V06', horaEvento, nomeEvento, carac, x]
                    listaE.append(listaC)
        c += 1
    return listaE
