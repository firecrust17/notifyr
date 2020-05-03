import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

from get_config import *


class EmailNotifyr:

	def __init__(self):

		self.email_from = config_json['config']['mail_config']['email_from']
		self.email_to = [config_json['config']['mail_config']['email_to']]
		self.cc = None
		self.msg = ''
		self.username = config_json['config']['mail_config']['email_username']
		self.password = config_json['config']['mail_config']['email_password']

		self.server = smtplib.SMTP('smtp.gmail.com:587')
		# self.server.ehlo()
		self.server.starttls()
		self.server.login(self.username,self.password)

	def send_mail(self, subject, body, to=[], cc=[]):
		if to:
			self.email_to = to 

		self.msg = MIMEMultipart('alternative')
		self.msg['From'] = formataddr((str(Header('Notifyr', 'utf-8')), self.email_from))
		self.msg['To'] = ", ".join(self.email_to)
		if cc:
			self.msg['CC'] = ", ".join(cc)
			self.email_to = self.email_to + cc
		self.msg['Subject'] = subject
		self.msg.attach(MIMEText(body, 'html'))

		self.server.sendmail(self.email_from, self.email_to, self.msg.as_string())


if __name__ == "__main__":
    # obj = EmailNotifyr()
    # obj.send_mail("hello subject", "email <b>bhejdi</b>", ['email1@gmail.com'], ['email2@gmail.com', 'email3@gmail.com'])
    pass