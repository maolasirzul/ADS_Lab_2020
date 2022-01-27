#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:28:29 2021

@author: maolasirzul
Description: Recursion
"""

#=================Task1===============

import time

start_time = time.time()




def bad_fibonacci(n):
  """Return the nth Fibonacci number."""
  if n <= 1:
    return n
  else:
    return bad_fibonacci(n-2) + bad_fibonacci(n-1)
print(bad_fibonacci(-1))
end_time = time.time()
print("\nRunning time  bad fibonacci: ", end_time-start_time)

def good_fibonacci(n):
  """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
  if n <= 1:
    return (n,0)
  else:
    (a, b) = good_fibonacci(n-1)
    return (a+b, a)

good = good_fibonacci(-1)
print("\nRunning time for good fibonacci: ",good,end_time-start_time)


