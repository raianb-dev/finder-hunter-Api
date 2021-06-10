from finder import Class, Export

#Autenticando api
api = Class.Class()

while api.Autenticar() != True:
    api.Autenticar()
    if api.Autenticar == True:
      break
      
#Recebendo dados para buscar
company = str(input('Company: '))
email = api.domain_search(company='{}'.format(company))


#Criando Um DataFrame
create = Class.Class()
df = create.CreateDf(email)

#Exportando para uma arquivo Csv
out = Export.Export()
out.Save(df)




