

class Node:
    def __init__(self, key):
        self.key= key
        self.next= None

class Queue:
    def __init__(self):
        self.emptyObject= Node(None) 
        self.head= self.emptyObject
        self.tail= self.emptyObject

    def enqueue(self, node):
        if self.emptyObject.next == None:
            self.emptyObject.next= node
            node.next= None
            self.head= node
            self.tail= node
        else:
            node.next= None
            self.tail.next= node
            self.tail= node

    def dequeue(self):
        if self.head == self.emptyObject and self.tail == self.emptyObject:
            print('Underflow')
        else:
            if self.head == self.tail:
                self.emptyObject.next= self.head.next
                self.head= self.emptyObject
                self.tail= self.emptyObject
            else:    
                self.emptyObject.next= self.head.next
                self.head= self.head.next

    def __str__(self):
        tempList= []
        temp= self.head
        
        while temp.next != None:
            tempList.append(temp.key)
            temp= temp.next
        
        tempList.append(temp.key)
        return 'The elements in the queue are: %s' % tempList

if __name__ == '__main__':
    node1, node2, node3, node4= Node(1), Node(5), Node(4), Node(8)
    list1= Queue()
    list1.enqueue(node1)
    list1.enqueue(node2)
    list1.enqueue(node3)
    list1.enqueue(node4)
    print(list1)
    list1.dequeue()
    print(list1)
    list1.dequeue()
    print(list1)
    list1.dequeue()
    print(list1)
    list1.dequeue()
    print(list1)
    list1.dequeue()
    print(list1)

                                                   