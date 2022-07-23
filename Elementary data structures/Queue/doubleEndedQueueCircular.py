"""
Implementation of double ended queue. We can enqueue and dequeue in double ended queue or deque form front as 
well as from back.The head will represent the memory location where front element will be inserted. Initially
it would be length of array subtracted by 1, the tail would represent the memory location where element from 
the back will be inserted, initially it would be zero.The overflow condition for insertion from front as well 
as from back is, if head is equal to tail. The underflow condition for dequeueing from the front as well as 
from back is whether tail == (head + 1) % n. 
"""

class Deque:
    """
    class Dequeue which defines two dundar methods and other four methods named enqueueBack, dequeueBack, 
    enqueueFront, dequeueFront
    """
    def __init__(self, size):
        self.array = [None for x in range(size)]
        self.length = size
        self.head = self.length - 1
        self.tail = 0
        

    def enqueueBack(self, x: int):
        if self.head == self.tail: 
            print('Overflow')
        else:
            self.array[self.tail] = x
            self.tail = (self.tail + 1) % self.length

    def dequeueFront(self)-> int:
        if self.tail == (self.head + 1) % self.length:
            print('Underflow')
        else:
            self.head = (self.head + 1) % self.length
            x = self.array[self.head]
            return x

    def enqueueFront(self, x: int):
        if self.head == self.tail:
            print('Overflow')
        else:
            self.array[self.head] = x
            self.head = (self.head - 1) % self.length
            

    def dequeBack(self)-> int:
        if self.tail == (self.head + 1) % self.length:
            print('Underflow')
        else:
            self.tail = (self.tail - 1) % self.length
            return self.array[self.tail]
    
    def __repr__(self):
        tempList = []
        head= self.head
        tail= self.tail
        while tail != (head + 1) % self.length:
             head = (head + 1) % self.length
             tempList.append(self.array[head])
        return 'Elements of the double ended queue are %s' % tempList

def main():
    instance = Deque(7)
    instance.dequeueFront()
    instance.dequeBack()
    instance.enqueueBack(1)
    instance.enqueueBack(2)
    instance.enqueueBack(3)
    instance.enqueueBack(4)
    instance.enqueueFront(5)
    instance.enqueueFront(6)
    print(instance)
    instance.enqueueFront(7)
    print(instance)
    element = instance.dequeBack()
    print(f'The element dequeued from back is {element}')
    print(instance)
    instance.dequeueFront()
    instance.dequeueFront()
    instance.dequeueFront()
    instance.dequeueFront()
    instance.dequeueFront()
    print(instance)
    instance.dequeueFront()
    

if __name__ == '__main__':
    main()
                            



                                                