"""
Implementation of hashtable using double hashing in which first hash function is h1(k) = k, and second hash
function is h2(k) = 1 + (k mod (m - 1)). On average the insertion, deletion and search is going to take O(1)
time.
"""
class HashTable:
    """
    class HashTable defining two operating overloading methods and four other methods named hashfunction, 
    insert, delete and search.
    """
    def __init__(self, size: int):
        self.hashtable = [None for i in range(size)]
        self.length = size
        self.c1 = 0
        self.c2 = 1

    def hashfunction(self, element: int, i: int)-> int:
        """
        This function calculates the key value in which the element will be inserted
        """
        return (element + i * self.hashfunctionSecond(element)) % self.length
    
    def hashfunctionSecond(self, element: int)-> int:
        """
        Second hash function 
        """
        return 1 + (element % self.length - 1)


    def insert(self, element: int)-> None:
        """
        The insert function is going to probe all the slot sequences given by double hashing, if he finds the 
        slot associated with the key is None or it is 'd'(indication of element was present there but deleted)
        it is going to insert the element there.
        """
        for i in range(self.length):
            key = self.hashfunction(element, i)
            if self.hashtable[key] == None or self.hashtable[key] == 'd':
                self.hashtable[key]= element
                break
        else:
            print('Overflow')

    def delete(self, element: int) -> None:
        """
        delete function will first search the key associated with the element, if it is present then it will
        put 'd' in that slot, otherwise it will print element not found
        """
        key= self.search(element)
        if isinstance(key, str):
            print('element not found')
        else:
            self.hashtable[key]= 'd'

    def search(self, element: int) -> object:
        """
        search function similar to insert is going to probe all the sequences given by double hashing
        and if element at slot matches with the element given, then it will return the key, otherwise it 
        will return element not present
        """
        for i in range(self.length):
            key = self.hashfunction(element, i)
            if self.hashtable[key] == element:
                return key
            if self.hashtable == 'd':
                continue
            if self.hashtable == None:
                return 'element not present'
        else:
            return 'element not present'
    

    def __repr__(self):
        return str(self.hashtable)
def main():
    instance = HashTable(11)
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
    instance.insert(26)
    instance.insert(50)
    print(instance)
    instance.delete(6)
    print(instance)

if __name__ == '__main__':
    main()                                                            