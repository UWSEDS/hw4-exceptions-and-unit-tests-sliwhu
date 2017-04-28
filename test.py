import unittest
import os
import urllib.request as ur
from main import get_data, remove_data

class TestMethods(unittest.TestCase):
	#test file is present locally
	def test_LocalPresent(self):
		print ('test_LocalPresent: ')
		filename='4xy5-26gy.csv'
		try:
			os.remove(filename)
		except:
			pass
		test_url ='https://data.seattle.gov/resource/4xy5-26gy.csv'
		file=ur.urlopen(test_url)
		with open(filename, 'wb') as output:
			output.write(file.read())
		self.assertEqual(get_data(test_url), 303) 
		os.remove(filename)

	#test file not present locally
	def test_LocalnotPresent(self):
		print ('test_LocalnotPresent: ')
		filename='4xy5-26gy.csv'
		try:
			os.remove(filename)
		except:
			pass
		test_url='https://data.seattle.gov/resource/4xy5-26gy.csv'
		self.assertEqual(get_data(test_url), 304)

	#test url not valid
	def test_GeturlInvalid(self):
		print ('test_GeturlInvalid: ')
		test_url='http://invalid'
		self.assertEqual(get_data(test_url), 305)
	

	#test remove file if file exist
	def test_RemoveLocalPresent(self):
		print ('test_RemoveLocalPresent: ')
		filename='4xy5-26gy.csv'
		try:
			os.remove(filename)
		except:
			pass
		test_url='https://data.seattle.gov/resource/4xy5-26gy.csv'
		file=ur.urlopen(test_url)
		with open(filename, 'wb') as output:
			output.write(file.read())
		self.assertEqual(remove_data(test_url), 303) 	
		try:
			os.remove(filename)
		except:
			pass

	def test_RemoveLocalnotPresent(self):
		print ('test_RemoveLocalnotPresent: ')
		filename='4xy5-26gy.csv'
		try:
			os.remove(filename)
		except:
			pass
		test_url='https://data.seattle.gov/resource/4xy5-26gy.csv'
		self.assertEqual(remove_data(test_url), 304) 
	
	def test_RemoveurlInvalid(self):
		print ('test_RemoveurlInvalid: ')
		test_url='http://invalid'
		self.assertEqual(remove_data(test_url), 305)

if __name__ == '__main__':
    unittest.main()