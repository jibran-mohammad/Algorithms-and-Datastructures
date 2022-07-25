"""
Implemention of union operation of two doubly linked lists. The time complexity of this operation is O(1)
"""
import doublyCircularLinkedList as DD 

class Union(DD.LinkedList):
    """
    class Union inheriting the linkedlist class of doublycircular linked lists. It defines one operator 
    overlaoding method __or__ and one union method. The instances of this union class can appear in bar operator
    which will be treated as union operation.
    """
    def union(self, list2):
        if self.emptyObject.prev == None and self.emptyObject.next == None and list2.emptyObject.prev == None and list2.emptyObject.next == None:
            print('Both Lists are empty')
        elif self.emptyObject.prev == None and self.emptyObject.next == None and list2.emptyObject.prev != None and list2.emptyObject.next != None:
            concatenatedList= list2
            return concatenatedList
        elif self.emptyObject.prev != None and self.emptyObject.next != None and list2.emptyObject.prev == None and list2.emptyObject.next == None:
            concatenatedList= self
            return concatenatedList
        else:            	
            self.emptyObject.prev.next= list2.emptyObject.next
            list2.emptyObject.next.prev= self.emptyObject.prev
            self.emptyObject.prev= list2.emptyObject.prev
            list2.emptyObject.prev.next= self.emptyObject
            list2.emptyObject.prev= list2.emptyObject.next= None
            concatenatedList= self
            return concatenatedList
    
    def __or__(self, other):
        return self.union(other)

def main():
    list1= Union()
    list2= Union()
    node1, node2, node3, node4= DD.Node(1), DD.Node(5), DD.Node(8), DD.Node(54)
    list1.insert(node1)
    list1.insert(node2)
    list1.insert(node3)
    list1.insert(node4)
    print(list1)
    node5, node6, node7= DD.Node(34), DD.Node(56), DD.Node(23)
    list2.insert(node5)
    list2.insert(node6)
    list2.insert(node7)
    print(list2)
    resultList= list1.union(list2)
    print(resultList)
    resultedList= list1 | list2
    print(resultedList)


if __name__ == '__main__':
    main()