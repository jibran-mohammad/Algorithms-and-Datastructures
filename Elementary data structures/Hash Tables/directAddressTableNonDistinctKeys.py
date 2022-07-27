"""
Implementation of direct address table with non distinct keys. The objects with the same keys are stored in
a doubly linked list whose empty objects address is present in the location key. Insert, delete and search 
operation will take O(1) time
"""

class Node:
    """
    class Node defining the strucuture of the node in doubly linked list
    """
    def __init__(self, key: int):
        self.left = None
        self.key = key
        self.right = None

class DoublyLinkedList:
    """
    class DoublyLinkedList defining two operating overloading methods and other methods named insert and delete
    """
    def __init__(self):
        self.emptyObject = Node(None)

    def insert(self, node: Node)-> None:
        if self.emptyObject.right == None:
            self.emptyObject.right = node
            node.left = self.emptyObject
            node.right = self.emptyObject
            self.emptyObject.left = node
        else:
            node.left= self.emptyObject.right.left
            node.right = self.emptyObject.right
            self.emptyObject.right.left = node
            self.emptyObject.right = node

    def delete(self, node: Node)-> None:
        node.left.right = node.right
        node.right.left = node.left
        node.left = None
        node.right = None

    def __repr__(self):
        temp = self.emptyObject.right
        tempList = []
        while temp != self.emptyObject:
            tempList.append(temp.key)
            temp = temp.right
        return f'{tempList}'    

class DirectAddress(DoublyLinkedList):
    """
    class DirectAddress defining two operating overloading methods and other methods named insert, delete and 
    search
    """
    def __init__(self, size: int):
        self.array= [None for i in range(size)]
        self.length = size
        self.instances = [None for i in range(size)]

    def insert(self, key: int, node: int)-> None:
        if self.array[key] == None:
           dll =DoublyLinkedList()
           dll.insert(node)
           self.instances[key] = dll
           self.array[key] = dll.emptyObject
        else:
           self.instances[key].insert(node)

    def delete(self, key: int, node: int= None) -> None:
        if self.array[key] == None:
            print('no node present in the given key')
        else:    
            self.instances[key].delete(node)

    def search(self, key: int)-> bool:
        if self.array[key] == None:
            return False
        else:
            return True

    def __repr__(self):
        return f'The elements inside the direct address table are{[[self.instances[i]] for i in range(self.length)]}'
    
def main():
    nodeList = [Node(78), Node(34), Node(55), Node(90), Node(23), Node(67)]
    instance = DirectAddress(10)
    instance.delete(2,)
    instance.insert(5, nodeList[0])
    instance.insert(5, nodeList[1]) 
    instance.insert(5, nodeList[2])
    instance.insert(8, nodeList[3])
    instance.insert(1, nodeList[4])
    instance.insert(1, nodeList[5])  
    print(instance)
    instance.delete(5,nodeList[2]) 
    print(instance)
    instance.delete(1, nodeList[4])
    print(instance)
    print(instance.search(0))

if __name__=='__main__':
    main()    