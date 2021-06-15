import pandas as pd
from pyhunter import PyHunter as ph
import json
import requests
from time import sleep

class Conection:

  #Método Autênticar
  def Autenticar(self):
    
    self.api = str(input('Chave de API: '))
    #Conectando com Api
    self.response = requests.get(f"https://api.hunter.io/v2/account?api_key={self.api}")
    if self.response.status_code == 200:
      print('Conectado com Hunter.io!')
      return True
    else:
      print("Falhou! Tente novamente.")
      return False


  #Método Procurar
  def Procurar(self):
    
    self.emp = str(input('Buscar Coorporation: '))
    auth = ph(self.api)
    busca = auth.domain_search(company=f'{self.emp}')
    print('Extraindo Emails.')
    return busca

  #Método Createdf
  def CreateDf(self, df):
    self.df = pd.DataFrame(df)
    sleep(10)
    print('Concluido.')
    return self.df

  #listando informações da conta
  def Acount(self):
    self.all = json.loads(self.response.content)
    self.data = self.all['data']

    #armazenando primeiro nome
    self.name = self.data['first_name']

    #armazenando ultimo nome
    self.last_name = self.data['last_name']

    #armazenando plano de assinatura
    self.plan_name = self.data['plan_name']

    #armazenando quantidade de requisições
    self.requests = self.data['requests']
    
    #armazenado quantidade de buscas
    self.searches = self.requests['searches']
    self.used = self.searches['used']
    self.available = self.searches['available']
    
    #Exibir informações na interface
    print(f'####################################')
    print(f'##### Bem vindo, {self.name} {self.last_name} ######')
    print(f'###################################','\n')
    print(f'Plano de assinatura atual: {self.plan_name}.')
    print(f'Pesquisas disponíveis: {self.available}')
    print(f'Você usou: {self.used}.\n')
