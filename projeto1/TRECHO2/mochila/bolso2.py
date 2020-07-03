# BOLSO 2: etapa de relação e separação de especificidades.

def ajusteIntPreOp(dic_s):
    '''
        Retorna uma lista com o mesmo comprimento da lista de entrada.
        Com o 1º índice de cada lista elem convertido para inteiro.
    '''
    ### ALTERAR O _s1 PARA A FUNÇÃO SERVIR TAMBÉM PARA _s2.
    tam = len(dic_s[f'mainCol']) # Obter comprimento da coluna mainCol.
    c = 0
    li = list()
    # CRIAR NOVA MESMA COLUNA, MAS COM AS HORAS NO TYPE INTEIRO.
    while c < tam:
        liVar = list()
        var = dic_s[f'mainCol'][c][0] # Seleciona as horas.
        #print(f'1º elem da {c}ª linha: {int(var[0:2])}')
        liVar.append(int(var[0:2])) # Coloca na lista a conversão str -> int.
        i = 1
        # Recolocar as horas, convertidas, junto às outras informações do
        # elemento, e então coloca-los na nova lista.
        while i < (len(dic_s[f'mainCol'][c])): # Tamanho do elemento(c).
            # Receber todos os elementos da coluna velha, um por vez (c), e
            # receber todos as info de cada um desses elementos (i).
            var = dic_s[f'mainCol'][c][i]
            #print(f'{c}ª linha: {var}')
            liVar.append(var) # Sublista (liVar), pertencente à (li).
            # Se atingir o tamanho (i) do elemento (c), Então este elemento será
            # uma nova sublista anexada à lista principal (li).
            if i == (len(dic_s[f'mainCol'][c])-1):
                #print(liVar)    
                li.append(liVar) # anexação à lista principal (li).
            i += 1
        c += 1
    #print(li) # lista de listas. cada uma sublista é um elemento (evento).
    return li

def ajustoHora(li):
    #
    # SOMAR -1 (HORA) EM CADA ELEM DA LISTA S1, PARA EQUIVALER AO HORÁRIO S2.
    # RETORNA UMA LISTA COM O MESMO TAMANHO DA LISTA DE ENTRADA.
    #
    tam = len(li) # Obter comprimento da coluna mainCol.
    c = 0
    i = 0
    nNum = list()
    while c < tam:
        var2 = li[c][0]
        #print(f'Valor inicial da lista s1: {var}')
        # O resultado da subtração é colocado numa
        # lista auxiliar temporária de inteiros.
        nNum.append(var2-1) # Subtração direta do -1 à hora s1.
        #print(f'Novo valor da lista s1: {var}')
        c += 1
    #print('')
    #print(nNum)
    #print('')
    return nNum

def ajusteNovaLista(nNum, li):
    #
    # reCOLOCAR A LISTA S1 COM O NOVO HORÁRIO.
    # RETORNA UMA LISTA COM O MESMO TAMANHO DA LISTA DE ENTRADA.
    #
    tam = len(nNum) # Obter comprimento da coluna mainCol.
    liS1 = list()
    c = 0
    while c < tam: #
        liVar2 = list() # lista aux recriada a cada elem (c) da lista principal(mainCol).
        liVar2.append(nNum[c]) # Na 1ª posição da sublista elem: receber o horário já do type inteiro.
        #print(f' A primeira posição da lista {c}: {liVar2}')
        i = 1 # A 1ª posição é a hora. Já inserida na instrução anteior.
        while i < len(li[c]):
            var2 = li[c][i] # começando pela 2ª posição de cada sublista (elem == evento).
            #print(f'{c}ª linha: {var}')
            liVar2.append(var2)
            # Se atingir o tamanho do elem (c), Então é criada uma sublista
            # dentro da nova lista principal.
            if i == (len(li[c])-1):
                #print(f' A lista {c}: {liVar2}')
                liS1.append(liVar2) # Anexação da sublista elem à nova lista principal.
            i += 1
        c += 1
    #print(liS1)
    return liS1 # Nova lista principal, originária da mainCol.

def rel(liS2, liS1):
    '''
        rel(lista fixa ou de referência, lista a ser comparada)
        A lista de referência é fixada como (i), enquanto a outra lista é
        analisada (j) através da referência. Essa operação é realizada devido
        a mais elementos estarem relacionados, só vistos se houver
        uma referenciação mútua. Nesse sentido, é necessario usar a mesma lista,
        uma vez como referência e outra vez como analisada para um resultado
        mais abrangente.
    '''
    #
    # Relação da 1ª posição s1 com a 1ª posição s2.
    # SE forem iguais ENTÂO criar lista temporária com os matchs!
    #
    tamS1 = len(liS1)
    tamS2 = len(liS2)
    liAux = list()
    #liNewS1 = list()
    liNewS2 = list()
    i = 0
    cont = 0
    # Loop que fixa cada elem s2 (i) enquanto percorre s1 de um (j) por um (j).
    while i < tamS2: # A lista s2 toda.
        j = 0
        varS2_h = liS2[i][0] # s2. 1ª sublista (1º elem) da lista s2. (HORA).
        c = 0 # contador s2.
        #
        for j in range(tamS1):
            varS1_h = liS1[j][0] # s1. 1ª indice da sublista 1: horas no type inteiro.
            if varS2_h == varS1_h: # Se a hora é IGUAL.
                # Então recorta a componente 'nome' para serem comparados.
                elemS2 = liS2[i][2]
                elemS1 = liS1[j][2]
                # Se as 2 letras inicial dos nomes forem IGUAIS.
                if (elemS2[0:1]) == (elemS1[0:1]):
                    #
                    if c == 0: # ADICIONAR APENAS 1 VEZ À NOVA LISTA.                    
                        liNewS2.append(liS2[i])
                        c += 1
            j += 1
        i += 1
    #
    strERROR = '\nATENÇÃO: \nNão houve relação diária ou ainda não foi possível recolher \ntodas as informações necessárias. Ou seja, s2 deve ser \nbuscado 2 vezes por dia pra englobar o conteúdo do dia inteiro, \nporque se houver um grande número de elementos, uma única \nbusca diária não engloba o conteúdo diário por completo.'
    # RETORNA A LISTA DE MATCHING SE ELA NÃO ESTIVER VAZIA.
    if len(liNewS2) > 0:
        return liNewS2, len(liNewS2) # Retorna uma tupla.
    else:
        return strERROR, 0 # Retorna uma tupla.
