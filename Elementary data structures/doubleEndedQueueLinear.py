

class Deque:
    def __init__(self, size):
        self.array= [None for x in range(size)]
        self.head = -1
        self.tail = 0
        self.n = size

    def enqueueFront(self, x):
        if self.head == 0:
           print('Overflow')
        else:
           self.head = self.head - 1
           self.array[self.head] = x

    def dequeueFront(self):
        if self.head == self.tail:
            print('Underflow')
        else:
            x = self.array[self.head]
            self.head = self.head + 1
            return x

    def enquequeBack(self, x):
        if self.tail == self.n:
            print('Overflow')
        else:
            if self.head == -1:
        	    self.head = 0
        	    self.array[self.tail] = x
        	    self.tail = self.tail + 1
            else:    
                self.array[self.tail] = x
                self.tail = self.tail + 1

    def dequeueBack(self):
        if self.tail == self.head:
            print('Underflow')
        else:
            self.tail = self.tail - 1
            return self.array[self.tail]
    
    def __str__(self):
        tempList = []
        head = self.head
        tail = self.tail
        while head != tail:
            tempList.append(self.array[head])
            head = head + 1
        return 'Elements in the double ended linear Queue is : %s' % tempList
            
if __name__ == '__main__':
    instance = Deque(6)
    instance.enquequeBack(1)
    instance.enquequeBack(5)
    instance.enquequeBack(6)
    instance.enquequeBack(8) 
    print(instance)
    instance.enqueueFront(78)
    instance.dequeueFront()
    print(instance)
    instance.dequeueBack()
    print(instance)                                                     