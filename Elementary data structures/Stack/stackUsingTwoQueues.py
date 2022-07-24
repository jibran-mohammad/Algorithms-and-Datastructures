"""
Implementation of stack using two queues. Push operation takes O(1) time and pop operation takes O(n) time. The 
algorithm uses deque class in collection module to emulate queue
"""
from collections import deque
class StackUsingTwoQueues:
    """
    class StackUsingTwoQueues defining two dundar methods and two other methods push and pop
    """
    def __init__(self):
        self.queue1= deque()
        self.queue2= deque()

    def push(self, element: int)-> None:
        self.queue1.append(element)

    def pop(self)-> int:  
        if len(self.queue1) == 0:
            print('Underflow')
        else:      
            while len(self.queue1) != 1:
                element = self.queue1.popleft()
                self.queue2.append(element)       
            result = self.queue1.popleft()
            while len(self.queue2) != 0:
                element = self.queue2.popleft()
                self.queue1.append(element)
            return result
    
    def __repr__(self):                                   
        return f'The elements inside the stack are {self.queue1}'

def main():
    instance = StackUsingTwoQueues()
    instance.pop()
    instance.push(48)
    instance.push(2)
    instance.push(5)
    instance.push(66)
    instance.push(78)
    print(instance)
    element = instance.pop()
    print(f'The popped element is {element}')
    print(instance)
    element = instance.pop()
    print(f'The popped element is {element}')
    element = instance.pop() 
    print(f'The popped element is {element}') 
    element = instance.pop() 
    print(f'The popped element is {element}')
    element = instance.pop() 
    print(f'The popped element is {element}')
    element = instance.pop() 

if __name__ == '__main__':
    main()         