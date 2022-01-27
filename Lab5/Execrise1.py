#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:08:07 2021

@author: maolasirzul
Description: . Improve Bubble Sort
"""


def bubble_sort(arr, asc=True):
    n = len(arr)

    # Traverse through all array elements
    swapFlag = False
    
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

            if (asc and arr[j] > arr[j+1]) or (not asc and arr[j] < arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapFlag = True
                    

        if (swapFlag == False):
            break
        
# Tesing the given number
arr = [1, 3, 18, 10 ]
bubble_sort(arr)

print("Sorted number are:")
for i in range(len(arr)):
    print ("%d" %arr[i])
