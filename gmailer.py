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

	def params(self):
		return self._params

	def email(self):
		return self._email

class Template:

	_subject = None
	_sbjrender = None

	_body = None
	_render = None

	def __init__(self, subject):
		self._subject = subject
		self._sbjrender = self._subject

	def render_params(self, params):
		for k in params.keys():
			self.replace_pair(k, params[k])

	def replace_pair(self, key, value):
		self._render = self._render.replace("{{"+str(key)+"}}", str(value))
		self._sbjrender = self._sbjrender.replace("{{"+str(key)+"}}", str(value))

	def content(self, body):
		self._body = body
		self._render = self._body

	def render(self, recipient):
		self._render = self._body
		self._sbjrender = self._subject

		if isinstance(recipient, Recipient):
			self.render_params(recipient.params())
		return self._render

	def subject(self):
		return self._sbjrender

class Gmailer:

	_sender = None
	_recipients = None
	_subject = None
	_body = None
	_template = None
	_html = False

	def __init__(self, sender):
		self._sender = sender
		self._recipients = []

	def add_recipient(self, *args):
		for e in list(args):
			self._recipients.append(e)

	def set_subject(self, subject):
		self._subject = subject

	def set_body(self, body, html = False):
		self._body = body
		self._html = html

	def set_template(self, template):
		self._template = template

	def get_subject(self):
		if self._template is not None:
			if self._template.subject() is not None:
				return self._template.subject()
		return self._subject

	def get_content(self, r):
		if self._template is not None:
				if isinstance(r, Recipient):
					return self._template.render(r)
				else:
					return self._template.render()
		else:
			return self._body

	def send(self):
		if self._sender is None:
			return False
		
		(sender_email, sender_passwd) = self._sender.get_credentials()

		for e in self._recipients:

			if isinstance(e, Recipient):
				recipient_email = e.email()
			else:
				recipient_email = e

			msg = MIMEMultipart()
			content = self.get_content(e)

			msg['From'] = sender_email
			msg['To'] = recipient_email
			msg['Subject'] = self.get_subject()

			msg.attach(MIMEText(content))

			mailServer = smtplib.SMTP("smtp.gmail.com", 587)
			mailServer.ehlo()
			mailServer.starttls()
			mailServer.ehlo()
			mailServer.login(sender_email, sender_passwd)
			mailServer.sendmail(sender_email, recipient_email, msg.as_string())
			# Should be mailServer.quit(), but that crashes...
			mailServer.close()