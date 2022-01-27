#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:51:29 2021

@author: maolasirzul
description: Countiing votes
"""




def max_vot(votes):
    small = big = votes[0] # assuming nonempty
    for val in votes:
        if val > big:
            big = val
    return small,big

print(max_vot(["john", "johnny", "jackie",
"johnny", "john", "jackie","jamie", "jamie", "john",
"johnny", "jamie", "johnny",
"john"]))

