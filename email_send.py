import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from settings import EMAIL
from settings import EMAIL_PASSWORD

def send_emails(data):
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(EMAIL,EMAIL_PASSWORD)
    image = open("dnu.png", 'rb').read()
    img_send = MIMEImage(image, name=os.path.basename("dnu.png"))
    for element in data:
        msg = MIMEMultipart()
        print(element)

        msg['From'] = EMAIL
        msg['To'] = element['email']
        msg['Subject'] = "Any subject!\n"
        msg_body = f'''Any text!
        '''
        msg.attach(MIMEText(msg_body))
        msg.attach(img_send)
        server.send_message(msg)
    print("Отправка завершена.")
