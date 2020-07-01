from mochila.bolso1 import *

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
