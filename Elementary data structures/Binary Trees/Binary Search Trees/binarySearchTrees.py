"""
Implementation of binary search tree with operations insert, delete, minimum, maximum, predecessor, successor,
search. All these operations will take O(h) time, where 'h' is the height of the tree. In worst case the 
binary tree will be a chain of nodes, in that case height will be O(n) where n is the number of nodes, and the
time complexity of all operations will be O(n), but on average the height of the binary search tree will be
O(n). There are methods for inorder, preorder and postorder traversal which takes O(n) time, where n represents
the number of nodes inside a tree, space complexity is also O(n). 
"""

class Node:
    """
    class Node defining the structure of the node in the binary search tree
    """
    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key

    def __repr__(self):
        return f'{self.key}'    

class BinarySearchTree:
    """
    class BinarySearchTree defining two operating overloading methods and some other methods named search,
    minimum, maximum, successor, predecessor, insert, delete.
    """
    def __init__(self):
        self.root = None

    def search(self, key: int)-> Node:
        """
        This method will start from the root and will check whether the root.key is less than the key given, 
        if it is, then left subtree will be considered, otherwise right subtree will be considered, the 
        procedure will continue until either the element is found, or it is not in the tree.
        """
        if self.root == None:
            print('Tree is empty')
        else:    
            temp = self.root
            while temp != None:
                if temp.key == key:
                    return temp
                elif temp.key < key:
                    temp = temp.right
                else:
                    temp = temp.left
            else: 
                return False

    def minimum(self, rootNode: Node)-> int:
        """
        The minimum element in the binary search tree will be present in the left subtree and it will be the
        leaf node at the last level, thus the procedure will move downward the tree until it reaches the 
        leave node.
        """
        if rootNode == None:
            print('Tree does not contain any element')
        else:    
            temp = rootNode
            while temp != None:
                minimum = temp.key
                temp = temp.left
            return minimum

    def maximum(self, rootNode: Node)-> int:
        """
        The maximum element will be present in the right subtree and it will be the leaf node. Thus procedure
        moves downward in the tree until it hits the leaf node in the right subtree
        """
        if rootNode == None:
            print('Tree does not contain any elements')
        else:
            temp = rootNode
            while temp != None:
                maximum = temp.key
                temp = temp.right      
            return maximum 
    
    def successor(self, node: Node)-> str:
        """
        In this procedure we are finding out inorder successor of an element, which means finding out the 
        next element to be processed in inorder fashion. Two conditions will occur, if the node has the 
        right subtree, then the minimum element in that right subtree will be the node which will be next visited
        If it doesn't have the right subtree, then the successor will be the closest ancestor of the node, for 
        which the node is the left child.
        """
        if node == None:
            return 'Tree is empty'
        elif node.left == node.right == None:
            return 'Element has no Successor'
        else:
            if node.right != None:
                return str(self.minimum(node.right))
            else:
                parent = node.parent
                while parent != Null and parent.right == node:
                    node = parent
                    parent = node.parent
                if parent == None:
                    return 'Element has no successor'
                else:
                    return str(parent.key)

    def predecessor(self, node: Node)-> str:
        """
        In this procedure we are finding inorder predecessor which means the node which was previously visited
        in inorder fashion. Two conditions will occur, if the node has left subtree, then the predecessor will
        be the maximum element in the left subtree, if it doesn't have the left subtree, then the predecessor
        will the closest ancestor of which the node is right child.
        """
        if node == None:
            return "Tree doesn't contain any elements"
        elif node.left == node.right == None:
            return 'Element has no predecessor'
        else:
            if node.left != None:
                return str(self.maximum(node.left))
            else:
                parent = node.parent
                while parent != None and parent.left == node:
                    node = parent
                    parent = node.parent
                if parent == None:
                    return 'Element has no predecessor'
                else:
                    return str(parent.key)

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

    def inorder(self, rootNode: Node)-> None:
        """
        This is the tree traversal in which the root is printed in the middle of the left subtree and right
        subtree.
        """
        if self.root == None:
           print('Tree is empty')
        elif rootNode == None:
            return   
        else:
            self.inorder(rootNode.left)
            print(rootNode.key, end = ' ')
            self.inorder(rootNode.right)   

    def preorder(self, rootNode: Node)-> None:
        """
        This is the tree traversal in which the root is printed before the left and right subtree
        """
        if self.root == None:
            print('Tree is empty')
        elif rootNode == None:
            return     
        else:
            print(rootNode.key, end = ' ')
            self.preorder(rootNode.left)
            self.preorder(rootNode.right)   

    def postorder(self, rootNode: Node) -> None:
        """
        This is the tree traversal in which the root is printed after the left and right subtree nodes
        """
        if self.root == None:
            print('Tree is empty')
        elif rootNode == None:
            return    
        else:
            self.postorder(rootNode.left)
            self.postorder(rootNode.right)
            print(rootNode.key, end = ' ')   

    def delete(self, node: Node)-> None:
        """
        Three conditions will occurr for deletion of the node in binary search tree
        1) If the node you want to delete has neither left nor right children, then we can delete it by changing
        the parent's pointers.
        2) If the node you want to delete has only one child, either left or right, then we have to elevate
        the child to the nodes position.
        3) If the node you want to delete has both children, then find the inorder successor which will be in
        the right subtree, now if the successor is the right child of node we want to delete, then we simply
        elevate the right child in place of node, if it isn't the immediate right child of node, then replace
        the successor(it will only have right child) with its right child and replace the node with the 
        successor.
        """
        if node.left == None and node.right == None:
            if node == node.parent.right:
                node.parent.right = None
            elif node == node.parent.left:
                node.parent.left = None
        elif node.left == None and node.right != None:
            if node == node.parent.right:
                node.parent.right = node.right
                node.right = None
            elif node == node.parent.left:
                node.parent.left = node.right
                node.right = None
        elif node.right == None and node.left != None:
            if node == node.parent.right:
                node.parent.right = node.left
                node.left.parent = node.parent
                node.parent = None
                node.left = None
            elif node == node.parent.left:
                node.parent.left = node.left
                node.left.parent = node.parent
                node.parent = None
                node.left = None
        elif node.right != None and node.left != None:
            success = self.minimum(node.right)
            success = self.search(success)
            if success == node.right:
                success.left = node.left
                if node == node.parent.left:
                    node.parent.left = node.right
                    node.right.parent = node.parent
                    node.parent = None
                    node.right = None
                elif node == node.parent.right:
                    node.parent.right = node.right
                    node.right.parent = node.parent
                    node.parent = None
                    node.right = None
            else:
                if success == success.parent.left:
                    success.parent.left = success.right
                    if success.right != None:
                        success.right.parent = success.parent
                elif success == sucess.parent.right:
                    success.parent.right = success.right
                    if success.right != None:
                        success.right.parent = success                                                             
                success.left = node.left
                success.right = node.right
                success.parent = node.parent
                if node.parent == None:
                    success.parent = None
                    self.root = success 
                elif node == node.parent.left:
                    node.parent.left = success
                elif node == node.parent.right:
                    node.parent.right = success  
            node.left = None
            node.right = None
            node.parent = None           

def main():
    instance = BinarySearchTree()  
    instance.search(4)
    instance.minimum(instance.root)
    instance.maximum(instance.root)
    print(instance.predecessor(instance.root))
    print(instance.successor(instance.root))
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
    instance.preorder(instance.root); print()
    instance.postorder(instance.root); print()
    instance.inorder(instance.root); print()
    print(instance.search(16))
    print(instance.search(480))
    print(f"Minimum = {instance.minimum(instance.root)}")
    print(f"Maximum = {instance.maximum(instance.root)}")
    print(f"Predecessor of 12 = {instance.predecessor( instance.search(12) ) }")
    print(f"Predecessor of 6 ={instance.predecessor(instance.search(6) ) }")
    print(f"Successor of 20 ={instance.successor(instance.search(20))}")
    print(f"Successor of 27 ={instance.successor(instance.search(27))}")
    instance.delete(instance.search(20))
    instance.inorder(instance.root); print()
    instance.delete(instance.search(15))
    instance.inorder(instance.root)
    instance.delete(instance.search(12)); print()
    instance.inorder(instance.root)
    

if __name__ == '__main__':
    main()    
