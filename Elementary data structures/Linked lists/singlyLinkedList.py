"""
Implementation of singly linked list supporting operation insert, delete and search. Insert and delete will
take O(1) time given the node to be deleted in singly linked list and search will take O(n) time.
"""

class Node:
    """
    class Node defining the attributes of objects inside the singly linked list.
    """
    def __init__(self, key):
        self.key= key
        self.next= None

class LinkedList:
    """
    class LinkedList defining two operating overloading methods and three other methods insert, delete and
    search
    """
    def __init__(self):
        self.emptyObject= Node(None)

    def insert(self, node):
        if self.emptyObject.next == None:
            self.emptyObject.next= node
            node.next= None
        else:
            node.next= self.emptyObject.next
            self.emptyObject.next= node

    def delete(self, node):
        if self.emptyObject.next == None:
            print('Underflow')
        else:    
            temp= self.emptyObject.next

            while temp.next.key != node.key:
                temp= temp.next

        temp.next= node.next

    def search(self, k):
        temp= self.emptyObject.next
        while temp.key != k and temp.next != None:
            temp= temp.next
        if temp.key == k:
            return temp 
        else:
            return 'key not found'            

    def __str__(self):
        tempList = []
        temp = self.emptyObject.next
        while temp.next != None:
            tempList.append(temp.key)
            temp= temp.next
        tempList.append(temp.key)
        return 'The keys of the linked list are: %s' % tempList

def main():
    node1, node2, node3, node4 = Node(1), Node(3), Node(5), Node(8)
    list1= LinkedList()
    list1.insert(node1)
    list1.insert(node2)
    list1.insert(node3)
    list1.insert(node4)
    print(list1)
    list1.delete(node3)
    print(list1)
    list1.insert(Node(66))
    print(list1)
    print(list1.search(66).key)
    print(list1.search(34))

if __name__ == '__main__':
    main()    