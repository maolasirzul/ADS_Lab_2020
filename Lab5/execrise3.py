#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:11:44 2021

@author: maolasirzul
description:. Sort by sum digits
"""

def sum_number(arr): 
	digits = [int(digit) for digit in str(arr) ] 
	return sum(digits) 
	
# Driver Code 
arr = [12, 10, 106, 31, 15]
arr_2 = [14, 1101, 10, 35, 0] 
print(sorted(arr, key =sum_number))
print(sorted(arr_2, key=sum_number))


