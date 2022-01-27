#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:51:05 2021

@author: maolasirzul
Description: Recursion
"""

#=================Task2===============

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.backward(lineLen)
        myTurtle.right(5)
        drawSpiral(myTurtle,lineLen-10)

drawSpiral(myTurtle,100)
myWin.exitonclick()