# Import sys library that allows interaction with the interpreter
import sys
# We import os to do basic interaction with command line
import os
# Imported to access class that manages files with unseroted and sorted lists
import manage_files as filemanager
# Imported to have access to module that contains sorting algorithms themseleves
import sorting_algorithms as sortalgr


def main():
	
	# We delete all possible txt files where previous sorted and non-sorted
	# lists could be stored
	os.system('rm *.txt')

	# Let's clean screen for user
	os.system('clear')

	# We request user to provide file that contain non-sorted numbers...
	file_name = raw_input('Provide name of file with non-sorted random numbers ')
	
	# ... and also ask her/him to provide the largest number in file...
	max_num = raw_input('Provide maximum integer number in the list of non-sorted numbers ')
	# ... and change it from string to integer
	max_num = int(max_num)

	# Let's intantiate class with name of file and maximum integer provided
	file_number = filemanager.ManageFiles(max_num,file_name+'.txt')

	# We firstly create file containing non-sorted numbers...
	file_number.file_random_numbers()

	# ... and read file to an auxiliary list
	x_unsorted = file_number.read_numbers()

	# If we wish we could print to screen the list of non-sorted arrays
	#print x_unsorted

	"""
		The following commented lines exemplify how each sorting
		algorithm can be used from sorting_algorithms module. They are,
		however, integreted into one single function called 
		sorting_algorithm. It's use is shown below
	"""

	#y = sortalgr.bubble_sort(x_unsorted)
	#y = sortalgr.selection_sort(x_unsorted)
	#y = sortalgr.merge_sort(x_unsorted)
	#y = sortalgr.quick_sort(x_unsorted,'middle')
	#y = sortalgr.qsort(x_unsorted)
	#y = sortalgr.shell_sort(x_unsorted)
	#y = sortalgr.heap_sort(x_unsorted)


	"""
		Once we have the non-sorted list of numbers we can choose an algorithm
		to perform the sorting. Options are:

			1. bubble
			2. selection
			3. merge
			4. quick (pivot chosen to be the middle of list)
			5. shell
			6. heap

		Here we use, for exemplification, quick sort

	"""

	# We sort the list with the chosen algorithm, store it 
	# in list y and...
	y = sortalgr.sorting_algorithm(x_unsorted,'quick')

	# ...print it to file named 'sorted_list.txt'
	file_number.file_sorted(y,'sorted_list.txt')
	
    
# Typical execution line...
if __name__ == '__main__':
    main()
