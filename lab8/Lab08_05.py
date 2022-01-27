#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:10:05 2021

@author: maolasirzul
"""

def Palindrome(S):
    return s== s[::-1]
def find_all_Palindrome():
    list_all - list()
    for line in  open("LAb08_05.py"):
        words - line.strip().lower().split()
        for x in word:
            if palindrome(x):
                list_all.append(x)
    return list_all

palindrome_list - find_all_Palindrome()

print("The unique word are",palindrome_list)