#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

class Sender:
	
	_email = None
	_passwd = None

	def __init__(self, email, passwd):
		self._email = email
		self._password = passwd

	def get_credentials(self):
		return (self._email, self._password)

class Recipient:

	_email = None
	_params = None

	def __init__(self, email, params = dict()):
		self._email = email
		self._params = params

	def set_params(self, params):
		self._params = params

	def params(self, params):
		return self._params

	def email(self):
		return email

class Template:

	_content = None

	def __init__(self, content):
		self._content = content

	def render_params(self, params):
		for k in params.keys()
			self.replace_pair(k, params[k])

	def replace_pair(self, key, value):
		self._content.replace("{{"+key+"}}", value)

	def content(self, recipient = None):
		if recipient is not None:
			self.render_params(recipient.params())
		return self._content

class Gmailer:

	_sender = None
	_recipients = None
	_subject = None
	_body = None
	_html = False

	def __init__(self, sender):
		self._sender = sender
		self._recipients = list()

	def add_recipients(self, *args):
		for e in list(args):
			self._recipients.append(e)

	def set_subject(self, subject):
		self._subject = subject

	def set_body(self, body, html = False):
		self._body = body
		self._html = html

	def get_content(self):
		if self._template is not None:
			return self._template
		else
			return self._body

	def send(self):
		if self._sender is None:
			return False
		
		(sender_email, sender_passwd) = self._sender.get_credentials()

		for e in self._recipients:

			if isinstance(e, Recipient)
				recipient_email = e.email()
			else
				recipient_email = e

			msg = MIMEMultipart()

			msg['From'] = sender_email
			msg['To'] = recipient_email
			msg['Subject'] = self._subject

			msg.attach(MIMEText(self._body))

			mailServer = smtplib.SMTP("smtp.gmail.com", 587)
			mailServer.ehlo()
			mailServer.starttls()
			mailServer.ehlo()
			mailServer.login(sender_email, sender_passwd)
			mailServer.sendmail(sender_email, e, msg.as_string())
			# Should be mailServer.quit(), but that crashes...
			mailServer.close()