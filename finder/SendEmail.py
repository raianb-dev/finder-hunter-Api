import smtplib
from email.message import EmailMessage

Sender_Email = input("Seu email: ")
Password = input('Password: ')
Reciever_Email = input("Remetente: ")


newMessage = EmailMessage()                         
newMessage['Subject'] = "Sua tabela de Csv." 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('Segue abaixo o anexo da sua tabele de emails') 

files = ['DropboxRelatorio.csv']


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)   