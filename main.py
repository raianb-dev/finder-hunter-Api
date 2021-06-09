from Class import classe
from pyhunter import PyHunter as ph


api = ph('my_hunter_api_key')

#Finder All e-mails
comp = str(input('Company :'))
email = api.domain_search(company=f'{comp}')

df = classe.Data(email)
df.exibir()