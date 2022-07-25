"""
Iterative implementation of reversal of the linked list. The time complexity of this algorithm is O(n) and 
space complexity if O(1)
"""
import singlyLinkedList as SL 

class Reverse(SL.LinkedList):
    """
    class Reverse inheriting from Linked List class in singlyLinkedList module and defining method reverse
    """
    def reverse(self):
        prev= None
        cur= self.emptyObject.next
      
        while cur:
            nex= cur.next
            cur.next= prev
            prev= cur
            cur= nex
        self.emptyObject.next = prev

def main():
    node1, node2, node3, node4 = SL.Node(1), SL.Node(3), SL.Node(5), SL.Node(8)
    list1= Reverse()
    list1.insert(node1)
    list1.insert(node2)
    list1.insert(node3)
    list1.insert(node4)
    print(list1)
    list1.reverse()
    print(list1)  
if __name__ == '__main__':
    main()          

                     
