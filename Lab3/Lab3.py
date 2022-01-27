"""Author: Maola Sirzul
Date:02/02/2021
Description:ArrayStack implementation """
from _queue import Empty


class ArrayStack:
    # stack crated
    def __init__(self):
        self._data = []

    # return the number of element in the stack
    def __len__(self):
        return len(self._data)

    #     return  if the stack in empty
    def empty_data(self):
        return len(self._data) == 0

    # adding element
    def push(self, element):
        self._data.append(element)
    def top(self):
        if self.empty_data():
            raise Empty('Stack is empty')

    #         remove and return the element
    def pop(self):
        if self.empty_data():
            raise Empty("Stack is empty")
        else:
            return self._data.pop()





