

class Deque:
    def __init__(self, size):
        self.array = [None for x in range(size)]
        self.head = -1
        self.tail = 0
        self.n = size

    def enqueueBack(self, x):
        if self.head == (self.tail + 1) % self.n: 
            print('Overflow')
        elif self.head == -1:
            self.head = 0
            self.array[self.tail] = x
            self.tail = (self.tail + 1) % self.n 
        else:
            self.array[self.tail] = x
            self.tail = (self.tail + 1) % self.n 

    def dequeueFront(self):
        if self.head == self.tail | self.head == -1:
            print('Underflow')
        else:
            x = self.array[self.head]
            self.head = (self.head + 1) % self.n 
            return x

    def enqueueFront(self, x):
        if self.head == (self.tail + 1) % self.n:
            print('Overflow')
        elif self.head == -1:
            self.head = 0
            self.array[self.head]= x
        else:
            self.head = (self.head - 1) % self.n
            self.array[self.head] = x

    def dequeBack(self):
        if self.head == self.tail:
            print('Underflow')
        else:
            self.tail = (self.tail - 1) % self.n 
            return self.array[self.tail]
    def __str__(self):
        tempList =[]
        head = self.head
        tail = self.tail
        while head != tail:
            tempList.append(self.array[head])
            head = (head + 1) % self.n
        return 'Elements of the double ended queue are [%s]' % tempList

if __name__ == '__main__':
    instance = Deque(8)
    instance.enqueueBack(1)
    instance.enqueueBack(2)
    instance.enqueueBack(3)
    instance.enqueueBack(4)
    instance.enqueueBack(5)
    instance.enqueueBack(6)
    instance.enqueueBack(7)
    print(instance)
    instance.dequeBack()
    print(instance)
    instance.enqueueFront(16)
    print(instance)
    instance.dequeueFront()
    print(instance)
    instance.enqueueBack(18)
    print(instance) 
    instance.enqueueBack(19)
                            



                                                