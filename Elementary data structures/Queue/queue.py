"""
Implementation of Queue. It is a FIFO datastructure where enqueue operation takes O(1) time and dequeue operation
takes O(1) time. The Queue has two attributes, head and tail. The elements are dequeued from head and elements
are inserted form the tail. The overflow condition for the insertion is if head is equal to tail plus 1 mod of n
The underflow condition for the queue is, if the head is equal to tail or head is -1.
"""

class Queue:
    """
    Class Queue with two dundar methods and three other methods named queueEmpty, enqueue, and dequeue
    """
    def __init__(self, size: int):
        self.array = [ None for x in range(size)]
        self.head = -1
        self.tail = 0
        self.length = size

    def queueEmpty(self) -> bool:
        """
        This method check whether the queue is empty, if it is return True, otherwise returns False
        """    
        if self.head == self.tail | self.head == -1:
            return True
        else:
            return False    

    def enqueue(self, x):
        """
        This method will insert the element inside the queue
        """
        if self.head == (self.tail + 1)  % self.length:
            print('Overflow')
        elif self.head == -1:
            self.head = 0
            self.array[self.tail] = x
            self.tail = (self.tail + 1) % self.length 
        else:
             self.array[self.tail] = x
             self.tail = (self.tail + 1) % self.length 

    def dequeue(self):
        """
        This method will delete the element from the queue
        """
        if self.queueEmpty(): 
            print('Underflow')
        else:
            x = self.array[self.head]
            self.head = (self.head + 1) % self.length
            return x
    
    def __repr__(self):
        tempList = []
        head = self.head
        tail = self.tail
        while head != tail  :
            tempList.append(self.array[head])
            head = (head + 1) % self.length
        return 'Elements of the queue are: %s' % tempList    

def main():
    instance = Queue(6)
    instance.dequeue() 
    instance.enqueue(4)
    instance.enqueue(6)
    instance.enqueue(8)
    instance.enqueue(15)
    instance.enqueue(5)
    print(instance.dequeue())
    instance.enqueue(78)
    instance.enqueue(44)
    print(instance)

if __name__ == '__main__':
   main() 

