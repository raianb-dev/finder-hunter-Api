import pandas as pd
from pyhunter import PyHunter as ph

class Class:

  #Método Autênticar
  def Autenticar(self, api):
    self.auth = str(api)
    self.con = ph(api)
    if self.auth != '':
      print('Conectado!')
    else:
      print("'Api falhou ao conectar'",type(self.auth))      
    return self.con

  #Método Procurar
  def Procurar(self, comp):
    ph.domain_search(company=comp)
    self.company = comp  

  #Método Createdf
  def CreateDf(self, var):
    self.var = pd.DataFrame(var)
    print(self.var)
    return
