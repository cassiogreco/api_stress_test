#!/usr/bin/env python

import unittest
from request_threads import RequestThreads

class StressTest(unittest.TestCase):

	# Change this number to stress check your system
	NUMBER_THREADS = 100

	def __init__(self, *args):
		super(StressTest, self).__init__(*args)
		self._get_threads = []
		self._post_threads = []
		for i in range(self.NUMBER_THREADS):
			self._get_threads.append(
				RequestThreads(
					i,
					'GET Thread' + str(i),
					'GET',
				)
			)
			self._post_threads.append(
				RequestThreads(
					i,
					'POST Thread' + str(i),
					'POST',
				)
			)

	def test_get_requests(self):
		counter = 0
		for i in range(self.NUMBER_THREADS):
			counter += 1
			self._get_threads[i].start()
		if counter == self.NUMBER_THREADS:
			self.assertTrue(True)

	def test_post_requests(self):
		counter = 0
		for i in range(self.NUMBER_THREADS):
			counter += 1
			self._post_threads[i].start()
		if counter == self.NUMBER_THREADS:
			self.assertTrue(True)

if __name__ == "__main__":
	unittest.main()
