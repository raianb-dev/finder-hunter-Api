import pandas as pd
from pyhunter import PyHunter as ph

class Data:
  def __init__(self, var):
    self.var = pd.DataFrame(var)
  
  def exibir(self):
    print(self.create)


class Conection:
  def __init__(self):
    self.key = '53ad5d83b0e3e0a6fc32b75ea0fcafaa3d65d15b'
    self.api = str(ph(self.key))
    print('Conectado com Api')
  