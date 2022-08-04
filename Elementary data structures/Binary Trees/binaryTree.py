"""
Binary tree Implemetation with insert and inorder traversal method. Insert will take O(h) time where h is the
height of the tree and inorder traversal will take O(n) time where n is the number of nodes. Space complexity of 
inorder traversal is O(n) time used by stack. Inorder traversal uses iterative algorithm.
"""

class Node:
    def __init__(self, key):
        self.left= None
        self.key= key
        self.right= None
        self.parent= None

class Tree:
    def __init__(self):
        self.root= None
        self.stack = []

    def insert(self, node: Node)-> str:
        """
        For insertion of the node, we have to find its proper position, for that we will compare the key of the
        node with the key of the root, if it's less than root key, then we consider the left subtree, otherwise
        we consider the right subtree, and we will continue this procedure until we reach the the leaf nodes.
        """
        if self.root == None:
            self.root = node 
            node.parent = None
        else:
            temp = self.root 
            while temp != None:
                if temp.key < node.key:
                    temp1 = temp
                    temp= temp.right
                else:
                    temp1 = temp
                    temp = temp.left 
            if temp1.key < node.key:
                temp1.right = node 
                node.parent = temp1
            else:
                temp1.left = node 
                node.parent = temp1
    
    def inorder_Traversal(self):
        current = self.root
        while True:
            if current is not None:
                self.stack.append(current)
                current = current.left
            elif self.stack:
                current  = self.stack.pop()
                print(current.key, end = ' ')
                current = current.right
            else:
                break
      


def main():
    instance = Tree()
    instance.insert(Node(15))
    instance.insert(Node(10))
    instance.insert(Node(20))
    instance.insert(Node(8))
    instance.insert(Node(12))
    instance.insert(Node(17))
    instance.insert(Node(25))
    instance.insert(Node(6))
    instance.insert(Node(11))
    instance.insert(Node(16))
    instance.insert(Node(27)) 
    instance.inorder_Traversal()       

if __name__=='__main__':
   main() 



            
