from gestorMain import *

# Captura.
s1_url = 'https://br.tradingview.com/markets/currencies/economic-calendar/'
s1_IDbuscado = "calendar-entry"
s1 = captura(s1_url, s1_IDbuscado)
#
s2_url = 'https://fbs.eu/en/analytics/calendar?type=currency'
s2_IDbuscado = "list_currency"
s2 = captura(s2_url, s2_IDbuscado)
#
# Decepamento.
dic_s1, dic_s2 = decepamento(s1, s2)
#
# Preparação do relacionamento.
liS1, liS2 = ajuste(dic_s1, dic_s2)
#
# RELACIONAMENTO s2 <-> s1.
Li, flag = relacio(liS2, liS1) # (lista referência, lista analisada).
#
print(Li)
print(flag)
