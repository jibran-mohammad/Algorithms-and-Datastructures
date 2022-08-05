

from binarySearchTrees import BinarySearchTree, Node
class BST(BinarySearchTree):
    def numberOfNodes(self, node: Node)-> int:
        if node == None:
            return 0
        elif node.left == None and node.right == None:
            return 1
        else:
            return 1 + self.numberOfNodes(node.left) + self.numberOfNodes(node.right)

    def numberOfLeafNodes(self, node: Node)-> int:
        if node == None:
            return 0
        elif node.left == None and node.right == None:
            return 1
        else:
            return self.numberOfLeafNodes(node.left) + self.numberOfLeafNodes(node.right)
    
    def numberOfNonLeaves(self, node: Node)-> int:
        if node == None:
            return 0
        elif node.left == None and node.right == None:
            return 0
        else:
            return 1 + self.numberOfNonLeaves(node.left) + self.numberOfNonLeaves(node.right)        
                          

def main():
    instance = BST()
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
    print(f"Number of nodes = {instance.numberOfNodes(instance.root)}")
    print(f"Number of leaf nodes = {instance.numberOfLeafNodes(instance.root)}")
    print(f"Number of non leaves = {instance.numberOfNonLeaves(instance.root)}")

if __name__ == '__main__':
    main()    
                
        