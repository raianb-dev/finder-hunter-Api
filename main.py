from finder import Class, Export

#Recebendo Chave de Api
key = str(input('Chave de Api: '))

#Autenticando com Hunter.io
auth = Class.Class()
conn = auth.Autenticar(key)

#Recebendo dados para buscar
company = str(input('Company: '))
email = conn.domain_search(company='{}'.format(company))

#Criando Um DataFrame
conn = Class.Class()
df = conn.CreateDf(email)

#Exportando para uma arquivo Csv
out = Export.Export()
out.Save(df)




