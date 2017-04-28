import unittest
import os
import urllib.request as ur
from main import get_data, remove_data

class TestMethods(unitest.TestCase):
	#test file is present locally
	def test_LocalPresent(self):
		test_url='https://data.seattle.gov/resource/4xy5-26gy.csv'
		file=ur.urlopen(test_url)
		with open('test.csv', 'wb') as output:
			output.write(file.read())
		self.assertFalse(get_data(test_url)) 

	def test_LocalnotPresent(self):
		test_url='https://data.seattle.gov/resource/4xy5-26gy.csv'
		self.assertTrue(get_data(test_url))

	def test_urlInvalid(self):
		test_url='http://invalid'
		self.assertFalse(get_data(test_url))

	def test_RemoveExist(self):
		return

if __name__ == '__main__':
    unittest.main()