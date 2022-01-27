"""Author: Maola Sirzul
Date:08/02/2021
Description:Reversed Stack"""
# Function to create a stack.
# It initializes size of stack
# as 0
def createStack():
    stack = []
    return stack


# Function to check if
# the stack is empty
def isEmpty(stack):
    return len(stack) == 0


# Function to push an
# item to stack
def push(stack, item):
    stack.append(item)



# Function to print the stack
def prints(stack):
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end=' ')
    print()


# Driver Code

stack = createStack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))

print("Reversed Stack" )
prints(stack)
