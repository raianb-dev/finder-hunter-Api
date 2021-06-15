from finder import Class, Export


#Autenticando api
api = Class.Conection()

while api.Autenticar() != True:
    api.Autenticar()
    if api.Autenticar == True:
      break

#Informações da Conta
api.Acount()
loop = ''
while loop == '':
  #Recebendo dados para buscar
  email = api.Procurar()


  #Criando Um DataFrame
  df = api.CreateDf(email)

  #Exportando para uma arquivo Csv
  out = Export.Export()
  out.Rename(df)

  sair = str( input( '\nPRESSIONE "ENTER" PARA CONTINUAR\nOU "QUALQUER TECLA" PARA SAIR...\n' ) )
  if sair:
    exit('Saindo')



