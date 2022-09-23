from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	random.seed(seed)
	list_of_num = []
	for i in range(number):
		list_of_num.append(i)
	random.shuffle(list_of_num)
	result = list_of_num
	return result

def generate():
	number = 10
	seed = 200
	
	# call gen_random_int() with the given number and seed
	# store it to the variable array
	pass
	array_str = ''
	array = gen_random_int(number, seed)
	for i in range(len(array)):
		array_str += array[i]
		if i == len(array)-1:
			array_str += '.'
			
		else:
			array_str += ','
	
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

def bubble_sort(array):
	n = len(array)-1
	for i in range(n):
		for inner in range (n):
			first_number = array[inner]
			second_number = array[inner+1]
			if(first_number> second_number):
				array[inner] = second_number
				array[inner+1] = first_number 
 


def sortnumber1():

	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	random_str = document.getElementById("generate").innerHTML
	temp_list = random_str.split(',')

	temp_list[len(temp_list)-1]= temp_list[len(temp_list)-1].split('.')[0]
	for i in range(len(temp_list)):
		temp_list[i] = int(temp_list[i])

	bubble_sort(temp_list)

	array_str = ''
	for i in range(len(temp_list)):
		array_str += str(temp_list[i])
		if i == len(temp_list)-1:
			array_str += '.'
			
		else:
			array_str += ','
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementById("numbers").value
 
	temp_list = value.split(',')

	temp_list[len(temp_list)-1]= temp_list[len(temp_list)-1].split('.')[0]
	for i in range(len(temp_list)):
		temp_list[i] = int(temp_list[i])


	# Throw alert and stop if nosthing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	
	bubble_sort(temp_list)

	array_str = ''
	for i in range(len(temp_list)):
		array_str += str(temp_list[i])
		if i == len(temp_list)-1:
			array_str += '.'
			
		else:
			array_str += ','

	# Your code should start from here
	# store the final string to the variable array_str

	array_str = array_str

	document.getElementById("sorted").innerHTML = array_str


