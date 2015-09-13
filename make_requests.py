#!/usr/bin/env python

import requests

# Add the API endpoint
API_URL = ''

class HTTPRequests:

	def __init__(self):
		pass

	@staticmethod
	def makeGetRequest():
		response = requests.get(API_URL)
		print('Response status code: {}'.format(response.status_code))

	@staticmethod
	def makePostRequest():
		response = requests.post(API_URL)
		print('Response status code: {}'.format(response.status_code))
