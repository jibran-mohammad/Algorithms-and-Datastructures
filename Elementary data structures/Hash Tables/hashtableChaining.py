"""
Implementation of hash table with chaining used as a collision resolution technique. The insertion will take O(1)
time and assumes that the object inserted doesn't already belong to the slot. The deletion will take O(1) time
on overage and similarly, the search will also take O(1) time on average. The asymptotic complexity of search
is proportional to the length of the doubly linked list used in chaining, but if we take the average values
it will turn out to be O(1)
"""

class Node:
    """
    class Node defining the structure of the node in doubly linked list
    """
    def __init__(self, key: int):
        self.prev = None
        self.data = key
        self.next = None

class DoublyLinkedList:
    """
    class Doubly Linked list defining operator overloading methods and some other methods names insert, delete.
    """
    def __init__(self):
        self.emptyObject = Node(None)

    def insert(self, node: Node)-> None:
        if self.emptyObject.next == None:
            self.emptyObject.prev = node
            self.emptyObject.next = node
            node.next = self.emptyObject
            node.prev = self.emptyObject
        else:    
            self.emptyObject.next.prev = node
            node.prev = self.emptyObject
            node.next = self.emptyObject.next
            self.emptyObject.next = node

    def delete(self, node: Node) -> None:
        if self.emptyObject.next == None:
            print('Linked list is empty')
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
    
    def __repr__(self):
        temp = self.emptyObject.next
        tempList = []
        while temp.data != None:
            tempList.append(temp.data)
            temp = temp.next
        return f'{tempList}'

class HashTable:
    """
    class HashTable using doubly linked list class using composition relationship and defining the two dundar
    methods and some other methods named hashfunction, insert, delete and search.
    """
    def __init__(self, size: int):
        self.hashtable = [None for i in range(size)]
        self.length = size
        self.lists = [None for i in range(size)]

    def hashfunction(self, data: int)-> int:
        return data % self.length

    def insert(self, data: int)-> None:
        key = self.hashfunction(data)
        if self.hashtable[key] == None:
            self.lists[key] = DoublyLinkedList()
            self.lists[key].insert(Node(data))
            self.hashtable[key] = self.lists[key].emptyObject
        else:
            self.lists[key].insert(Node(data))

    def delete(self, data: int)-> None:
        key = self.hashfunction(data)
        if self.hashtable[key] == None:
            print('The slot associated with the key is empty')
        else:
            temp = self.lists[key].emptyObject.next
            while temp.data != data:
                temp = temp.next
                if temp.data == None:
                    break    
            if temp.data == None:
                print('No element present inside the hash table')
            else:
                node = temp
            self.lists[key].delete(node)

    def search(self, data: int)-> None:
        key = self.hashfunction(data)
        if self.hashtable[key] == None:
            print('The slot of the hash table associated with the key is empty')
        else:
            temp = self.lists[key].emptyObject.next
            while temp.data != data:
                temp = temp.next
                if temp.data == None:
                    break    
            if temp.data == None:
                print('No element present inside the hash table')
            else:
                print(f'The element is present at the location {key}') 

    def __repr__(self):
        return f"The elements present inside the hash table are {[[self.lists[index]] for index in range(self.length)]}"               

def main():
    instance = HashTable(10)
    instance.search(44)
    instance.delete(45)
    instance.insert(56)
    instance.insert(34)
    instance.insert(24)
    instance.insert(0)
    instance.insert(76)
    instance.insert(78)
    instance.insert(12)
    instance.insert(99)
    print(instance)
    instance.insert(13) 
    instance.delete(34)
    print(instance)
    instance.search(12)

if __name__ == '__main__':
    main()           