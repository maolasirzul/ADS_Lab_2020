#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:03:45 2021

@author: maolasirzul
Description: Build that tree
"""

'''
    This is an example of a binary tree data structure created with 
    python lists as the underlying data structure.
'''


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


if __name__ == "__main__":
    root = BinaryTree("a")
    insertLeft(root, "b")
    insertRight(getLeftChild(root), "d")

    insertRight(root, "c")
    insertRight(getRightChild(root), "f")

    insertRight(getRightChild(root), "e")

print(root)
