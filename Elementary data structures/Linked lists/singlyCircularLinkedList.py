"""
Implementation of singly circular linked lists definig operation insert, delete and search. Insert , delete
will take O(1) time given the node to be deleted in the linked list and search will take O(n) time.
"""

class Node:
    """
    class Node represent the attributes of objects inside the linked list.
    """
    def __init__(self, key):
        self.key= key
        self.next= None

class LinkedList:
    """
    class LinkedList defining the two operating overloading methods and three other methods insert, delete and 
    search.
    """
    def __init__(self):
        self.emptyObject= Node(None)

    def insert(self, node):
        if self.emptyObject.next == None:
            self.emptyObject.next= node
            node.next= self.emptyObject
        else:
            node.next= self.emptyObject.next
            self.emptyObject.next= node

    def delete(self, node):
        if self.emptyObject.next == None:
            print('Underflow')
        else:
            temp= self.emptyObject.next
            while temp.next.key != node.key and temp != self.emptyObject:
                temp= temp.next

            temp.next= node.next

    def search(self, k):
        if self.emptyObject.next == None:
            print('Linked List is empty')
        else:
            temp= self.emptyObject.next
            while temp.key != k:
                temp= temp.next
            return temp.key                                            

    def __str__(self):
        tempList= []
        temp= self.emptyObject.next

        while temp != self.emptyObject:
            tempList.append(temp.key)
            temp= temp.next

        return 'The elements in the list are: %s' % tempList

def main():
    node1, node2, node3, node4= Node(1), Node(8), Node(7), Node(3)
    list1= LinkedList()
    list1.insert(node1)
    list1.insert(node2)
    list1.insert(node3)
    list1.insert(node4)
    print(list1)
    list1.delete(node3)
    print(list1)
    print(list1.search(1))
    print(list1)

if __name__ =='__main__':
    main()                        