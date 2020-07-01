from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def capturador(url, IDbuscado):
    '''
        Função scraping de captura a partir do id e caminho.
    '''
    # -- URL
    urlRec = url
    # -- CONFIG DE BUSCA.
    options = Options()
    options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\RS\AppData\Local\Programs\Python\Python37\chromedriver.exe')

    # -- ENTRADA.
    driver.get(urlRec)
    driver.set_page_load_timeout(5)

    # -- CONTEÚDO DE BUSCA.
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, IDbuscado))
            )
        var = main.text
    except:
        driver.quit()
    finally:
        driver.quit()

    # -- SAÍDA.
    driver.quit()
    return var


def decepamentoS1(s1):
    '''
        Função de decepamento da string s1. Retorna uma lista de listas
        na 1ª posição desse dicionário.
    '''
    x = s1.split('\n')
    #
    word = x[2] # dia de hoje.
    comp = word[0:3] # marcação de paragem: dia de amanhã.
    #
    # -- Migrar dados para uma lista.
    li = list()
    i = 3 # número correspondente ao 1º horário do 1º evento.
    while i <= (len(x)-1):
        li.append(x[i])
        i += 1
    #
    # -- Recortar apenas o dia atual.
    c = 0
    li2 = list()
    while c <= (len(li)-1):
        word2 = li[c]
        comp2 = word2[0:3] # dia posterior: para comparação.
        if comp2 == comp: # PARAR QUANDO OBTER A INFO DIÁRIA.
            c = (len(li)-2)
        else:
            li2.append(li[c])
        c +=1
    #
    # -- Armazenar de 3 em 3 linhas = 1 elemento.
    i = 0
    c = 0
    num = 0
    liS1 = list()
    while c <= (len(li2)-2):
        li3 = list()
        for i in range(3):
            li3.append(li2[c])
            c += 1
            if i == 2:
                liS1.append(li3) # guardar por elemento.
                num += 1
    dic = dict()
    dic['mainCol'] = liS1
    #
    return dic


def decepamentoS2(s2):
    '''
        Função de decepamento da string s2. Retorna uma lista de listas
        mais as horas, estas estão ainda soltas da lista de cada elemento.
    '''
    #
    x = s2.split('\n')
    #
    # -- Migrar dados para uma lista.
    li = list()
    i = 1 # número correspondente ao 1º horário do 1º evento.
    while i <= (len(x)-1):
        if (i%2 == 0): #
            a = x[i].split(' ')
            li.append(a)
        else:
            li.append(x[i])
        i += 1
    novodic = pd.DataFrame(li)
    #
    return novodic


def separS2(novodic):
    '''
        Função de separação do conteúdo necessário.
        Retorna um dicionário com uma lista de listas na sua 1ª posição.
        Filtrada pela necessidade do conteúdo 'var'.
    '''
    #
    d = novodic # Recebimento da 1ª posição do dicionário s2.
    tam = len(d)
    c = 0
    i = 0
    li = list()
    dic = dict()
    while c < tam:
        if c%2 != 0: #
                        # Tem-se a cronologia dos eventos.
            liAux = list()
            var = d[0][c][0] # primeiro índice de cada lista de conteúdo.
            if var == 'EUR':
                liAux.append(d[0][c-1]) # recebe a hora do evento.
                tamAux = len(d[0][c])
                num = 0
                while num < tamAux:
                    liAux.append(d[0][c][num]) # junta a hora ao restante.
                    num += 1
                li.append(liAux) # nova lista added à lista mainCol_s2.
            elif var == 'USD':
                liAux.append(d[0][c-1]) # recebe a hora do evento.
                tamAux = len(d[0][c])
                num = 0
                while num < tamAux:
                    liAux.append(d[0][c][num]) # junta a hora ao restante.
                    num += 1
                li.append(liAux) # nova lista added à lista mainCol_s2.
        c += 1
        #
    #
    dic['mainCol'] = li
    return dic


