
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configuração
host = 'smtp.gmail.com'
port = 587
user = ''
password = ''

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

# Login com servidor
print('Logando...')
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem
message = 'Olá, mundo!'
print('Criando mensagem...')
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = ''
email_msg['Subject'] = 'Assunto da mensagem'
print('Adicionando texto...')
email_msg.attach(MIMEText(message, 'plain'))

print('Obtendo arquivo...')
filename = 'Anoexo' 
filepath = '../out/Instagram-emails.csv'
attachment = open(filepath, 'rb')

print('Lendo arquivo...')
att = MIMEBase('application', 'octet-stream')
6*encoders.encode_base64(att)
att.add_header('Content-Disposition', f'attachment; filename= {filename}')

attachment.close()
print('Adicionando arquivo ao email...')
email_msg.attach(att)

# Enviando mensagem
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
print('Mensagem enviada!')
server.quit()
