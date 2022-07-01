
import singlyLinkedList as SL 

class Reverse(SL.LinkedList):
     def reverse(self):
         temp1= self.emptyObject.next
         temp2= self.emptyObject.next.next
         temp1.next= None
      
         while temp2 != None:
             temp3= temp2.next
             temp2.next= temp1
             temp1= temp2
             temp2= temp3
         else:
             self.emptyObject.next= temp1

if __name__ == '__main__':
    node1, node2, node3, node4 = SL.Node(1), SL.Node(3), SL.Node(5), SL.Node(8)
    list1= Reverse()
    list1.insert(node1)
    list1.insert(node2)
    list1.insert(node3)
    list1.insert(node4)
    print(list1)
    list1.reverse()
    print(list1)            

                     
