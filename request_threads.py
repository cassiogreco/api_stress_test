#!/usr/bin/env python

import threading
from make_requests import HTTPRequests

class RequestThreads(threading.Thread):

	GET_REQUEST = 'GET'
	POST_REQUEST = 'POST'

	def __init__(self, id, name, type_request):
		threading.Thread.__init__(self)
		self._id = id
		self._name = name
		self._type_request = type_request
		self._counter = 0

	def run(self):
		for i in range(10):
			self._counter += 1
			print('{} Making request number {}'.format(
				self._name,
				self._counter,
				)
			)
			if self._type_request == self.GET_REQUEST:
				HTTPRequests.makeGetRequest()
			elif self._type_request == self.POST_REQUEST:
				HTTPRequests.makePostRequest()
