#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:49:37 2021

@author: maolasirzul
Description: stack practice
"""
from collections import deque
stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    
    
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("91-IVOC ereuqnoc lliw eW"))
    print(reverse_string("I am the king"))
    print('#==========================Question-2==================')




def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

















































