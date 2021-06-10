from finder import Class, Export


#Autenticando api
api = Class.Conection()

while api.Autenticar() != True:
    api.Autenticar()
    if api.Autenticar == True:
      break

#Informações da Conta
api.Acount()

#Recebendo dados para buscar
company = str(input('Buscar por empresas: '))
email = api.domain_search(company='{}'.format(company))


#Criando Um DataFrame

df = api.CreateDf(email)

#Exportando para uma arquivo Csv
out = Export.Export()
out.Save(df)




