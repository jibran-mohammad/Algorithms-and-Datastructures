

class Node:
    def __init__(self, key):
        self.left= None
        self.key= key
        self.right= None
        self.parent= None

class Tree:
    def __init__(self):
        self.root= None

    def insert(self, key):
        node= Node(key)
        if self.root is None:
            self.root= node
            node.left= None
            node.right= None
            node.parent= None
        else:
            x= self.root
            while x != None:
                y= x
                if node.key < x.key:
                    x= x.left
                else:
                    x= x.right
            if node.key < y.key:
                y.left= node
            else:
                y.right= node
    
    def inorder_Traversal(self):
        x= self.root
        
if __name__=='__main__':
    tree= Tree()
    list1= [15,6,18,3,7,17,20,2,4,13,9]
    for element in list1:
        tree.insert(element)



            
