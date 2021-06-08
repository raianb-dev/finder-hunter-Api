import pandas as pd
from pyhunter import PyHunter as ph

class Data:
  def __init__(self, var):
    self.var = pd.DataFrame(var)
  
  def exibir(self):
    print(self.create)


class Conection:
  def __init__(self, api=False):
    self.api = str(ph(api))
    print('Conectado com Api')
  