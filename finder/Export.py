from finder import Class

class Export(Class.Class):
  def __init__(self, var):
    self.var.to_csv(f'{self.company}.csv', encoding='utf-8', index=False)
    print('Salvo com sucesso!')
    return 

  def Rename(self, df, nome):
    self.nome = str(input('Nome para o arquivo: '))
    df.to_csv(f'{self.nome}.csv', encoding='utf-8', index=False)
    print('Voce nomeou seu arquivo!')
    return

