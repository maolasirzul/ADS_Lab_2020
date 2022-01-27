#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:06:02 2021

@author: maolasirzul
Description: Recursion: Minimum & Maximum
"""

# =================Task3===============

import time

start_time = time.time()


def minmax(sequence):
    return min(sequence), max(sequence)


print(minmax([1, 2, 3, 5]))
print(minmax([0, 1, -2]))
print(minmax([3]))

end_time = time.time()

print("\nRunning time for Maximum:", end_time - start_time)
