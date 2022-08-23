import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from banco_de_emails import email
from time import sleep
from email.mime.image import MIMEImage
emails = email
# senha_anovoteto = "xrrmixwhwrsrcylh"

print(f'Gerando emails...')

for c in range(0, len(email)):
    endereco_gmail = "Seu email"
    senha_app = "Senha App"
    mail_de = 'Seu email'
    # Lista de emails
    mail_para = f"{email[c]}"
    # lista de emails end
    mail_assunto = "Assunto"
    mail_texto = 'Message text'

    # Direcionamento dos emails
    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_de
    mimemsg['To'] = mail_para
    mimemsg['Subject'] = mail_assunto

    # Adição do texto e imagem ao corpo do email - Towers
    '''text_html = MIMEText('')
       '''
    # imagem anexada
    with open('file name', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="file name")

    mimemsg.attach(MIMEText(mail_texto, 'plain'))
    mimemsg.attach(img)
    # mimemsg.attach(text_html)

    # Conctando servidor

    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(endereco_gmail, senha_app)
    connection.send_message(mimemsg)
    connection.quit()

print(f'{len(email)} emails enviados com sucesso')
sleep(3)
print("ENCERRANDO PROGRAMA")
sleep(3)
