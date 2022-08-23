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
    endereco_gmail = "corretormaylson@gmail.com"
    senha_app = "sigfkvjxinmdblls"
    mail_de = 'corretormaylson@gmail.com'
    mail_para = f"{email[c]}"
    mail_assunto = "ATENÇÃO - Timbé / Tijucas - Chácara 20.000 m²"
    mail_texto = '\nAgende agora uma visita! ' \
                 '\nContato: 48 99139-0999' \
                 '\nWhatsApp: https://api.whatsapp.com/send?phone=55489139-0999' \
                 '\nMais detalhes em nosso site: https://bityli.com/apIbSo'

    # Direcionamento dos emails
    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_de
    mimemsg['To'] = mail_para
    mimemsg['Subject'] = mail_assunto

    # Adição do texto e imagem ao corpo do email - Towers
    '''text_html = MIMEText(
        '<a href="https://sc.olx.com.br/florianopolis-e-regiao/imoveis/pronto-para-morar-amplo-apartamento-'
        '72-m-privativos-909534372"><img src="https://uploaddeimagens.com.br/images/003/370/846/original'
        '/Email_Towers.png?1628298831"></a>'
        '<h3><img src="https://uploaddeimagens.com.br/images/003/387/991/original/logo-whatsapp-verde-'
        'icone-ios-android-256.png?1629323880" alt="wpp.logo" width="25px" class="img-fluid" align="left">'
        'Whatsapp Corretor Maylson:<a href="https://api.whatsapp.com/send?phone=5548996761343">'
        '(48)99676-1343 </a></h3>'
        .format('body', 'Biguaçu Towers.png'), 'html')'''
    # imagem anexada Timbé
    with open('Timbé _Tijucas.png', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="Timbé _Tijucas.png")

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
