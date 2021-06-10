import pandas as pd
from pyhunter import PyHunter as ph
import requests

class Class:

  #Método Autênticar
  def Autenticar(self):
    
    self.api = str(input('Chave de api: '))

    self.response = requests.get(f"https://api.hunter.io/v2/account?api_key={self.api}")
    if self.response.status_code == 200:
      print('Conectado com Hunter.io!')
      return True
      pass
    else:
      print("Falhou! Tente novamente.")
      return False
    return 

  #Método Procurar
  def Procurar(self, comp):
    ph.domain_search(company=comp)
    self.company = comp  

  #Método Createdf
  def CreateDf(self, df):
    self.df = pd.DataFrame(df)
    return self.df