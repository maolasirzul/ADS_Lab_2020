#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 20:26:24 2021

@author: maolasirzul
description: . Tree size
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def count_nodes(self):
        self.data = + 1 data
    

def build_product_tree():
    root = TreeNode("My Number Tree")

    number_left = TreeNode("5")
    number_left.add_child(TreeNode("30"))
    number_left.add_child(TreeNode("40"))
    number_left.add_child(TreeNode("25"))

    number_right = TreeNode("2")
    number_right.add_child(TreeNode("4"))

    root.add_child(number_left)
    root.add_child(number_right)


    root.print_tree()

if __name__ == '__main__':
    build_product_tree()        