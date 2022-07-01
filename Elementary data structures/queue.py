

class Queue:
    def __init__(self, size):
        self.array = [ None for x in range(size)]
        self.head = -1
        self.tail = 0
        self.n = size

    def queueEmpty(self):
        if self.head == self.tail | self.head == -1:
            return True
        else:
            return False    

    def enqueue(self, x):
        if self.head == (self.tail + 1)  % self.n:
            print('Overflow')
        elif self.head == -1:
            self.head = 0
            self.array[self.tail] = x
            self.tail = (self.tail + 1) % self.n 
        else:
             self.array[self.tail] = x
             self.tail = (self.tail + 1) % self.n 

    def dequeue(self):
        if self.queueEmpty(): 
            print('Underflow')
        else:
            x = self.array[self.head]
            self.head = (self.head + 1) % self.n
            return x
    
    def __str__(self):
        tempList = []
        head = self.head
        tail = self.tail
        while head != tail  :
            tempList.append(self.array[head])
            head = (head + 1) % self.n
        return 'Elements of the queue are: %s' % tempList    

if __name__ == '__main__':
    instance = Queue(6)
    instance.dequeue() 
    instance.enqueue(4)
    instance.enqueue(6)
    instance.enqueue(8)
    instance.enqueue(15)
    instance.enqueue(5)
    print(instance.dequeue())
    instance.enqueue(78)
    print(instance)

