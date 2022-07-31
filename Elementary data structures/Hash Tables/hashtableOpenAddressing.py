"""
hash table implemented using open addressing with linear probing technique for getting the slot sequence, if there
is collision. The auxillary hash function used is h(k) = k. The time complexity for insertion, deletion and
search is O(1)
"""

class HashTable:
    """
    class HashTable defining two operating overloading methods and four other methods named hashfunction,
    insert, delete and search.
    """
    def __init__(self, size: int):
        self.hashtable= [None for i in range(size)]
        self.length = size

    def hashfunction(self, element: int, i: int)-> int:
        return (element + i) % self.length

    def insert(self, element: int)-> None:
        """
        The insert function is going to probe all the slot sequences given by linear probing, if he finds the 
        slot associated with the key is None or it is 'd'(indication of element was present there but deleted)
        it is going to insert the element there.
        """
        for i in range(self.length):
            key = self.hashfunction(element, i)
            if self.hashtable[key] == None or self.hashtable[key] == 'd':
                self.hashtable[key] = element
                break
        else:
            print('Overflow')

    def delete(self, element: int)-> None:
        """
        delete function will first search the key associated with the element, if it is present then it will
        put 'd' in that slot, otherwise it will print element not found
        """
        key = self.search(element)
        if isinstance(key, str):
            print(key)
        else:   
            self.hashtable[key] = 'd'

    def search(self, element: int)-> object:
        """
        search function similar to insert is going to probe all the sequences given by linear probing
        and if element at slot matches with the element given, then it will return the key, otherwise it 
        will return element not present
        """
        for i in range(self.length):
            key = self.hashfunction(element, i)
            if self.hashtable[key] == 'd':
                continue
            if self.hashtable[key] == element:
                return key
            if self.hashtable[key] == None:
                return 'element not present'
        else:
            return 'element not present'
    
    def __repr__(self):
        return str(self.hashtable)


def main():
    instance = HashTable(10)
    instance.insert(67)
    instance.insert(44)
    instance.insert(457)
    instance.insert(334)
    instance.insert(894)
    instance.insert(98)
    print(instance)
    key = instance.search(334)
    if isinstance(key, str):
        print(key)
    else:
        print(key) 
    key = instance.search(2)
    if isinstance(key, str):
        print(key)
    else:
        print(key)       
    instance.delete(44)
    print(instance)
    key =instance.search(894)
    if key == str:
        print(key)
    else:
        print(key)
    instance.insert(0)
    instance.insert(1)
    instance.insert(2)
    instance.insert(6)
    print(instance)
    instance.insert(56)
    print(instance)
    instance.insert(46)
    instance.delete(6)
    print(instance)
    instance.delete(6)

if __name__ == '__main__':
    main()                        
