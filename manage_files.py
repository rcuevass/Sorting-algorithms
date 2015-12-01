
# Imported to generate random number for sorting algorithms exemplification
import random

"""
	This module contains ManageFiles class that performs managment
	of files containing non-sorted and sorted lists of numbers
"""


class ManageFiles(object):

	"""
		One and only class in this module that contains functions managing creation
		of files with non-sorted and sorted lists of numbers for exemplification of
		sorting algorithms

	"""

	def __init__(self,max_num,file_name):

		"""
			Typical initialization class function
		"""
		# We intialize file name storing non-sorted values as well
		# as the maximum number in list
		self.file_name = file_name
		self.max_num = max_num

	def file_random_numbers(self):
		
		"""
			Function that creates a list of random numbers with maximum
			value max_num and stores them in file file_name. 
			Both max_num and file_name are provided by the user
		"""

		# Maximum value in list
		max_num = self.max_num
		# File name
		file_name = self.file_name
		# Generate random list of numbers
		thelist = random.sample(range(1, max_num+1), max_num)
		# Create file object...
		target = open(file_name, 'w')
		for item in thelist:
			# ... and print numbers to it
			target.write("%s\n" % item)

		# close file object
		target.close()
		

	def read_numbers(self):
		"""
			Function that allows reading values from 
			file
		"""
		file_name = self.file_name
		with open(file_name) as f:
			x = [int(line) for line in f]

		return x


	def file_sorted(self,x,file_name):
		"""
			Function that writes a list of values 
			x to file file_name
		"""
		target = open(file_name, 'w')
		for item in x:
			target.write("%s\n" % item)

		target.close()


