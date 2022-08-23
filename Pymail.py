import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from banco_de_emails import email
from time import sleep
from email.mime.image import MIMEImage

emails = email
print(f'Gerando emails...')
for c in range(0, len(email)):
    endereco_gmail = "desouza850@gmail.com"
    senha_app = "ueuturzcoikvhjdj"
    mail_de = "desouza850@gmail.com"
    mail_para = f"{email[c]}"
    mail_assunto = "ATENÇÃO - IMPORTANTE !!! "
    mail_texto = '\nENTRE EM CONTATO COM NOSSO CORRETOR "NOME DO CORRETOR":' \
                 ' https://api.whatsapp.com/send?phone=5548996761343'

# enviar foto
    with open('logo_pense_qmc.png', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="logo_pense_qmc.png")

    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_de
    mimemsg['To'] = mail_para
    mimemsg['Subject'] = mail_assunto
    # mimemsg.attach(img)
    # msgText = MIMEText(format('body'), 'html')
    # mimemsg.attach(msgText)

    mimemsg.attach(MIMEText(mail_texto, 'plain'))
    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(endereco_gmail, senha_app)
    connection.send_message(mimemsg)
    connection.quit()

print(f'{len(email)} emails enviados com sucesso')
sleep(3)
print("ENCERRANDO PROGRAMA")
sleep(3)
