"""
Implementation of stack using doubly linked list. Both push and pop operation takes O(1) time
"""

class Node:
    """
    Class Node defining the attributes present in the object contained in the linked list
    """
    def __init__(self, key):
        self.prev= None
        self.key= key
        self.next= None

class Stack:
    """
    Class Stack defining two operating overloading methods and two other methods push and pop
    """
    def __init__(self):
        self.emptyObject= Node(None)
        self.top= self.emptyObject
    
    def push(self, node):
        if self.emptyObject.next == None and self.emptyObject.prev == None:
            node.prev= self.emptyObject
            node.next= self.emptyObject
            self.emptyObject.next= node
            self.emptyObject.prev= node
            self.top= node
        else:
            self.emptyObject.prev.next= node
            node.prev= self.emptyObject.prev
            node.next= self.emptyObject
            self.emptyObject.prev= node
            self.top= node

    def pop(self):
        if self.top == self.emptyObject:
            print('Underflow')
        else:
            x= self.top.key
            self.top= self.top.prev
            self.top.next= self.emptyObject
            self.emptyObject.prev= self.top
            print('The popped element is ', x)

    def __str__(self):
        tempList= []
        temp= self.emptyObject.next
        
        while temp != self.top:
            tempList.append(temp.key)
            temp= temp.next
        tempList.append(temp.key)
        
        return 'The keys in the stack are: %s' % tempList

def main():
    node1, node2, node3, node4= Node(5), Node(3), Node(7), Node(65)
    list1= Stack()
    list1.push(node1)
    list1.push(node2)
    list1.push(node3)
    list1.push(node4)
    print(list1)
    list1.pop()
    print(list1)
    list1.pop()
    print(list1)
    list1.pop()
    list1.pop()
    list1.pop()
    print(list1)


if __name__ == '__main__':
   main() 

    