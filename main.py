from finder import Class

#Recebendo Chave de Api
key = str(input('Chave de Api: '))

#Autenticando com Hunter.io
auth = Class.FinderEmail()
conn = auth.Autenticar(key)

#Recebendo dados para buscar
company = str(input('Company: '))
email = conn.domain_search(company='{}'.format(company))

