#LIFO - last in first out
#FILO - first in last out

class Stack:
    def __init__(self,n):
        self.n = n
        self.stack = []

    #push - adding value to a stack
    def push(self,x):
        if len(self.stack) < self.n:
            self.stack.append(x)
            print("Number is added!")
        else:
            print("Stack is full!")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            self.stack.pop(-1)
            print("Number is removed!")

    def top(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            print(self.stack[-1])

    def size(self):
        a = len(self.stack)
        print("Number of elements in the stack:",a)

    def display(self):
        print(self.stack)




s = Stack(5)

s.push(6)
s.push(3)
s.push(8)
s.push(4)
s.push(5)
s.pop()
s.top()
s.size()
s.display()
s.push(11)
s.display()
s.push(15)
s.display()

