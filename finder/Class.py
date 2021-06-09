import pandas as pd
from pyhunter import PyHunter as ph

class CreateDf:
  def __init__(self, var):
    self.var = pd.DataFrame(var)
  
  def exibir(self):
    print(self.var)
    return

class FinderEmail:

  def Autenticar(self, api):
    self.auth = str(api)
    self.con = ph(api)
    if self.auth != '':
      print('Conectado!')
    else:
      print("'Api falhou ao conectar'",type(self.auth))      
    return self.con

  def Procurar(comp):
    ph.domain_search(company=comp)

