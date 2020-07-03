from gestorMain import *
from mochila.bolso3 import *

# Capt.
s1_url = 'https://br.tradingview.com/markets/currencies/economic-calendar/'
s1_IDbuscado = "calendar-entry"
s1 = capt(s1_url, s1_IDbuscado)
#
#s2_url = 'https://fbs.eu/en/analytics/calendar?type=currency'
x = '04-07-2020'
s2_url = f'https://fbs.eu/en/analytics/calendar?type=currency&calendarPeriod={x}%2C{x}&CalendarCurrenciesSearch%5Bimpacts%5D%5B0%5D=3&CalendarCurrenciesSearch%5Bimpacts%5D%5B1%5D=2'
s2_IDbuscado = "list_currency"
s2 = capt(s2_url, s2_IDbuscado)
#
# Dec.
dic_s1, dic_s2 = dec(s1, s2)
#
# Preparação do relacionamento.
liS1, liS2 = ajuste(dic_s1, dic_s2)
#
# RELACIONAMENTO s2 <-> s1.
Li, flag = relacio(liS2, liS1) # (lista referência, lista analisada).
#
#print(Li)
#print(flag)
#
# BPS2.
BPS2x = BPS2(Li) #
print(f'\nLista BPS2x: \n{BPS2x}')
#
