"""Author: Maola Sirzul
Date:02/02/2021
Description:Using ArrayStack """
from queue import Empty


class ArrayStack:
    # stack crated
    def __init__(self):
        self.data = []
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
            return self.data.pop()



if __name__ == "__main__":
    Stack = ArrayStack()
    Stack.push(5)
    Stack.push(3)
    print(Stack.data)
    print(Stack.pop())
    print(Stack.empty_data())
    Stack.push(7)
    Stack.push(9)
    Stack.push(4)
    print(Stack.pop())
    Stack.push(6)
    Stack.push(8)
    print(Stack.data)







