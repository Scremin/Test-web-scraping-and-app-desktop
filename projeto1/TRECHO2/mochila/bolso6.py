# BOLSO 6. FrontEnd.
from datetime import date, datetime
import pandas as pd

def preAjusteBin():
    '''
        Busca no arquivo pk1 a lista de listas salva na 1ª
        posição do dicionário principal.
        Retorna 2 listas com apenas as horas,
        para serem analisadas.
    '''
    b = pd.read_pickle('tmpSaveFrontEnd.pk1')
    f = len(b)

    site2 = b.at[0, 'ListaFront'] # 1ª linha. s2.
    site1 = b.at[1, 'ListaFront'] # 2ª linha. s1.

    if site1 == 0: # verificação de propagação de error s1.
        
        li_aux2 = list()
        d = 0
        while d < len(site2): #
            hora = site2[d][2]
            li_aux2.append(hora)
            d += 1
            
        return li_aux2, 0 # lista com as horas dos eventos e flag de error.
    
    else:
        
        li_aux2 = list()
        d = 0
        while d < len(site2): #
            hora = site2[d][2]
            li_aux2.append(hora)
            d += 1

        li_aux1 = list()
        d = 0
        while d < len(site1): #
            hora = site1[d][2]
            li_aux1.append(hora)
            d += 1
    
        return li_aux2, li_aux1 # lista com as horas dos eventos.

    
def ajusteHoraBin(listaHora):
    '''
        Função que recebe uma lista com os horários dos eventos
        diários. Retorna uma lista 'binária' com as posições
        correspondente aos eventos ainda válidos a serem
        printados no front.
    '''
    if listaHora == 0: # verificação de propagação de erro.
        return 0
    
    hora_atual = datetime.now()
    data_em_texto = hora_atual.strftime('%H:%M')
    print(data_em_texto)
    hr_atual = (data_em_texto[:2]) # recorte hora atual.
    #hr_atual = '11' # teste.

    hr_s = listaHora # horarios dos eventos recebidos do site. tupla
    print(hr_s)
    c = 0
    li = list()
    while c < len(hr_s): # Criar lista com a diferença de horário. a2
        #
        hr_atual = int(hr_atual) # conv to int.
        hr_s[c] = int(hr_s[c]) # conv to int. s2
        if (hr_s[c]>hr_atual):
            li.append(1) # operação de horários.
        else:
            li.append(25)
        c += 1
        print(li)
    return li


def printFinal(liBin2, liBin1):
    '''
        Versão 1 (atual): Recebe uma lista com 0 representando horários não
        úteis enquanto os 1 representam os horários válidos.
        Os horários válidos têm suas informações printadas no front.
        
        próx versão: 1 representam os horários mais próximos ao
        evento, mais próximo do horário atual.
        
        Retorna a lista principal do projeto, filtrada.
    '''
    b = pd.read_pickle('tmpSaveFrontEnd.pk1')
    f = len(b)
    
    site2 = b.at[0, 'ListaFront'] # 1ª linha.
    site1 = b.at[1, 'ListaFront'] # 2ª linha.
    
    if site1 == 0:

        liBin2 = liBin2
        liBin1 = liBin1
    
        hora_atual = datetime.now()
        data_em_texto = hora_atual.strftime('%H:%M')
        min_atual = (data_em_texto[-2:]) # minuto da hora atual.

        min_atual = int(min_atual) # conv to int.
        li_aux = list()
        d = 0
        while d < len(liBin2):
            if liBin2[d] == 1:
                #if min_atual != 3: # teste: 3 minutos após o evento ocorre a atualização.
                # horários ainda válidos.
                texto1 = site2[d][0]
                texto2 = site2[d][1]
                hora = site2[d][2]
                li_aux.append(f'{texto1}\nHorário de lançamento: {hora}\n{texto2}\nAtual: Ainda sem resultado.\n Nota: Ainda sem conclusão.')
                #else:
                #    pass
            else:
                pass
            d += 1

    else:

        liBin2 = liBin2
        liBin1 = liBin1
    
        hora_atual = datetime.now()
        data_em_texto = hora_atual.strftime('%H:%M')
        min_atual = (data_em_texto[-2:]) # minuto da hora atual.

        min_atual = int(min_atual) # conv to int.
        li_aux = list()
        d = 0
        while d < len(liBin2):
            if liBin2[d] == 1:
                #if min_atual != 3: # teste: 3 minutos após o evento ocorre a atualização.
                # horários ainda válidos.
                texto1 = site2[d][0]
                texto2 = site2[d][1]
                hora = site2[d][2]
                li_aux.append(f'{texto1}\nHorário de lançamento: {hora}\n{texto2}\nAtual: Ainda sem resultado.\n Nota: Ainda sem conclusão.')
                #else:
                #    pass
            else:
                pass
            d += 1

        d = 0
        while d < len(liBin1):
            if liBin1[d] == 1:
                #if min_atual != 3: # teste: 3 minutos após o evento ocorre a atualização.
                # horários ainda válidos.
                texto1 = site1[d][0]
                texto2 = site1[d][1]
                hora = site1[d][2]
                li_aux.append(f'{texto1}\nHorário de lançamento: {hora}\n{texto2}\nAtual: Ainda sem resultado.\n Nota: Ainda sem conclusão.')
                #else:
                #    pass
            else:
                pass
                #print('Valor fora do horário esperado')
            d += 1

    # aux do possivel print error para li_aux abaixo.
    data_atual = date.today()
    data_atual_texto = data_atual.strftime('%d/%m/%Y')
    
    #if len(li_aux) < 1: # Se a lista estiver vazia Então printa 'VAZIO'.
    #    li_aux = f'NENHUMA INFORMAÇÃO RECEBIDA OU APENAS\nNÃO HÁ MAIS INFORMAÇÕES PARA HOJE: {data_atual_texto}'

    return li_aux # retorna a lista a ser printanda no front.

