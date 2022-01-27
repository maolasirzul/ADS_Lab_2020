#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:41:36 2021

@author: maolasirzul
Description:Compare Linear and Binary Search
"""
import matplotlib.pyplot as plt
import numpy as np


def linearsearch(arr, n, x): 

	for i in range (0, n): 
		if (arr[i] == x): 
			return i; 
	return -1; 

# Driver Code 
arr = [ 1,3,9,10,18]; 
x = 18; 
n = len(arr); 
result_liner = linearsearch(arr, n, x) 
if(result_liner == -1): 
	print("Element is not present in array") 
else: 
	print("Element is present at index", result_liner); 
    
#-------------Binary search-------------
def binarySearch(arr, l, r, x): 

	while l <= r: 

		mid = l + (r - l) // 2; 
        # mid = left + (right - left) // 2 == (left + right) // 2
		
		# Check if x is present at mid 
		if arr[mid] == x: 
			return mid 

		# If x is greater, ignore left half 
		elif arr[mid] < x: 
			l = mid + 1

		# If x is smaller, ignore right half 
		else: 
			r = mid - 1
	
	# If we reach here, then the element 
	# was not present 
	return -1

# Driver Code 
arr = [ 1,3,9,10,18 ] 
x = 18
# Function call 
result_binary = binarySearch(arr, 0, len(arr)-1, x) 

if (result_binary != -1): 
	print ("Element is present at index % d" % result_binary) 
else: 
	print ("Element is not present in array")


#Plot the graph to see the difference in running time. 
plt.plot(result_liner,result_binary)
plt.xlabel('Linear')
plt.ylabel('Binary')
plt.title('running time(s)')
plt.show