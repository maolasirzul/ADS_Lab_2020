#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:41:22 2021

@author: maolasirzul
Description: Compare Bubble sort, Selection sort and Insertion sort
"""


# ================bubble sort==================
def bubble_sort(arr, asc=True):
    n = len(arr)

    # Traverse through all array elements
    swapFlag = False

    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            print("bubble sorting number:", j)

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

            if (asc and arr[j] > arr[j + 1]) or (not asc and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapFlag = True

        if (swapFlag == False):
            break


# Tesing the number
arr = [72, 9, 66, 48, 1, 10, 28, 33, 18, 8, 15, 7, 4, 6]
bubble_sort(arr)

print("Sorted number are:")
for i in range(len(arr)):
    print("%d" % arr[i])


# ===============selection sort ======================

def selection_sort(arr):
    for i in range(len(arr)):
        print("selection number:", i)

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

            # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Tesing the number
arr = [72, 9, 66, 48, 1, 10, 28, 33, 18, 8, 15, 7, 4, 6]
selection_sort(arr)

print("selection sorted number are:")
for i in range(len(arr)):
    print("%d" % arr[i])


# ===============Insertion sort ======================


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    # print("insertion sorted number are", j, arr[j], key)


# Tesing the number
arr = [72, 9, 66, 48, 1, 10, 28, 33, 18, 8, 15, 7, 4, 6]
insertion_sort(arr.sort())

print("insertion sorted number are:")
for i in range(len(arr)):
    print("%d" % arr[i])
