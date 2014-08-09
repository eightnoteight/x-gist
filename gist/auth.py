#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import requests
from requests.auth import HTTPBasicAuth
import json
from define import client
import os

class auth():
	"""docstring for auth"""
	def __init__(self):
		self.token    = ''
		self.username = ''
		self.password = ''
		self.app_details = 	{ 
								"scopes"	: ["gist"], 
								"note"		: client.name,
								"note_url"	: client.url
							}
	def get_credentials(self):
		self.username = str(raw_input('http://gist.github.com/ -- username  '))
		self.password = getpass.getpass('http://gist.github.com/ -- password  ')
	def get_token(self):
		self.token = self.read_token()
		return self.token
	def read_token(self):
		f_gist = open(os.getenv("HOME")+'/.x-gist','r')
		ret = f_gist.read()
		f_gist.close()
		return ret
	def write_token(self, write_this):
		open(os.getenv("HOME")+'/.x-gist','a').close()#touch
		f_gist = open(os.getenv("HOME")+'/.x-gist', 'w')
		f_gist.write(write_this)
		f_gist.close()
	def login(self):
		#for more info : https://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization
		response = requests.post('https://api.github.com/authorizations',
								 auth=HTTPBasicAuth(self.username, self.password),
								 data=json.dumps(self.app_details) )
		print response.status_code
		if response.status_code == 404:
			print 'Bad Credentials'
			raise BaseException
		elif response.status_code == 201:
			print 'Successfully logged in'
		elif response.status_code == 200:
			# saving for verbosity
			print 
		elif response.status_code == 422:
			print 'already exists'
			return
		self.token = response.json()['token']
		self.write_token(self.token)