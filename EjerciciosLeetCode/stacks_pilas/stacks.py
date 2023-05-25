"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

"""

class MinStack:
    def __init__(self):
        self.valores = []
        self.menoresHastaAqui = []

    def push(self, val: int) -> None:
        
        self.valores.append(val)
        if len(self.menoresHastaAqui)>0:
            if(val<self.menoresHastaAqui[-1]):
                self.menoresHastaAqui.append(val)
            else:
                self.menoresHastaAqui.append(self.menoresHastaAqui[-1])
        else:
            self.menoresHastaAqui.append(val)
            
    def pop(self) -> None:
        self.valores.pop()
        self.menoresHastaAqui.pop()

    def top(self) -> int:
        return self.valores[-1]

    def getMin(self) -> int:
        return self.menoresHastaAqui[-1]    

stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(0)
stack.push(1)
stack.pop()
print(stack.top())
print(stack.getMin())
stack.pop()
print(stack.getMin())