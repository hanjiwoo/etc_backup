from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

SERVER = 'smtp.gmail.com'
PORT = 465
USER = 'jiw021538@gmail.com'
PASSWORD = 35820215

def send_mail(name,addr):
	msg = MIMEMultipart()

	msg['From'] = USER
	msg['To'] = addr
	msg['Subject'] = '20420_한지우'
	contets = ''' python 메일 보내기 '''

	text = MIMEText(_text=contets, _charset='utf-8')
	msg.attach(text)

	smtp = smtplib.SMTP_SSL(SERVER,PORT)

	smtp.login(USER,PASSWORD)
	smtp.sendmail(USER,addr,msg.as_string())

	print("finish")

	smtp.close()


send_mail('정재웅선생님','skyjjw79@hanmail.net')