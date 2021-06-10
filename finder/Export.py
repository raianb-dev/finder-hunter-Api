from finder import Class

#Método Exportar 
class Export(Class.Conection):
  def Save (self, var):
    self.save = var.to_csv('out.csv', encoding='utf-8', index=False)
    print('Salvo com sucesso!')
    return var
    
  #Exportar com Rename
  def Rename(self, df, nome):
    self.nome = str(input('Nome para o arquivo: '))
    df.to_csv(f'{self.nome}.csv', encoding='utf-8', index=False)
    print('Voce nomeou seu arquivo!')
    return

