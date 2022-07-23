"""
Implementation Of Stack using array. It implements LIFO policy. The push and pop operation takes O(1) time.
"""

class Stack:
    """
    class Stack with two dundar methods and three other methods named stackEmpty, push, and pop.
    """
    def __init__(self, size: int):
        self.stack= [None for i in range(size)]
        self.length = size
        self.top = -1

    def stackEmpty(self)-> bool:
        """
        This method will check if the stack is empty, if it is, it will return True, otherwise returns False
        """
        if self.top == -1:
            return True
        else:
            return False

    def push(self, x):
        """
        This method is going to push the element in the stack
        """
        if self.top == self.length - 1:
            print('Overflow')
        else:    
            self.top += 1
            self.stack[self.top] = x

    def pop(self):
        """
        This method will pop the element from the stack
        """
        if self.stackEmpty():
            print('Stack is empty')
        else:
            self.top -= 1
            return self.stack[self.top + 1]
    
    def __str__(self):
        tempList = [self.stack[index] for index in range(self.length) if index <= self.top  ]
        return 'The stack is: %s' % tempList

def main():
    instance = Stack(6)
    instance.pop()
    instance.push(7)
    instance.push(1)
    print(instance)
    print(instance.pop())
    print(instance) 
    instance.push(78)
    instance.push(33)
    instance.push(89)
    instance.push(56)
    instance.push(72)
    instance.push(5)                                                   
    print(instance)

if __name__ == '__main__':
    main()