

class Node:
    def __init__(self, data):
        self.prev= None
        self.key= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.emptyObject= Node(None)

    def insert(self, node):
        if self.emptyObject.next == None and self.emptyObject.prev == None:
            node.next= self.emptyObject
            node.prev= self.emptyObject
            self.emptyObject.next= node
            self.emptyObject.prev= node 
        else:
            node.prev= self.emptyObject
            node.next= self.emptyObject.next    
            self.emptyObject.next.prev= node
            self.emptyObject.next= node
            

    def delete(self, node):
        node.prev.next= node.next
        node.next.prev= node.prev

    def search(self, k):
        x= self.emptyObject.next
        while x != self.emptyObject and x.key != k:
            x= x.next                   
        return x 
    
    def __str__(self):
        tempList = []
        x= self.emptyObject.next
        while x != self.emptyObject:
            tempList.append( x.key)
            x= x.next
        return 'Keys of the list are: %s' % tempList
            
if __name__ == '__main__':
    node1, node2, node3= Node(1), Node(5), Node(8)
    list1= LinkedList()
    list1.insert(node1)
    list1.insert(node2)
    list1.insert(node3)
    print(list1)
    x= list1.search(5)
    print(x.key)
    list1.delete(x)
    print(list1)
