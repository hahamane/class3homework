#!usr/bin/env python
import os

myFileName = "housing.data.txt"

if os.path.isfile(myFileName):
	print(myFileName + " exists")
else:
	print(myFileName + " does not exist")

with open(myFileName, 'r') as file_handle:
	for  line in file_handle.readlines():
		line_clean = line.replace ('   ',' ').replace('  ', ' ')
		line_clean = line_clean.strip()
		values = line_clean.split(' ')
		for value in values:
			print (float(value))

		
	
	print("finished!")	
# for homework: 
#identify what type of data each value is, and cast it
#to the appropriate type, then print the new, properly-typed 
#list to the screen
