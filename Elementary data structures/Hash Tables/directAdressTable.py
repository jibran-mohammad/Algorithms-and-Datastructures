"""
Implementation of direct address table of size n supporting the operations insert, delete, search and maximum
insert, delete and search takes O(1) time and maximum takes O(n) time.
"""

class DirectAddressTable:
    """
    class DirectAddressTable defining two operating overloading methods and four other methods insert, delete
    search and maximum.
    """
    def __init__(self, size: int):
        self.array= [None for i in range(size)]
        self.length= size

    def insert(self, key: int, object: int) -> None:
        self.array[key] = object

    def delete(self, key: int):
    	if self.array[key] == None:
    	    print(f'The location with key {key} is empty')
    	else:    
            self.array[key] = None

    def search(self, key: int) -> int:
        return self.array[key]             

    def maximum(self)-> int:
        maximum = float('-inf')
        for index in range(0,self.length):
            if self.array[index] == None:
               continue
            elif maximum < self.array[index]:
                maximum = self.array[index]
        return maximum
    
    def __repr__(self):
        return f'The objects inside the direct address table are {[self.array[i] for i in range(self.length)]}'

def main():
    instance = DirectAddressTable(10)
    instance.delete(4)
    instance.insert(5, 45)
    instance.insert(9, 34)
    instance.insert(8, 66)
    instance.insert(2, 56)
    print(instance)
    instance.delete(2)
    print(instance)
    element =  instance.search(8)
    print(f'The element at key 8 is {element}')
    maximum = instance.maximum()
    print(f'The maximum element inside an array is {maximum}')
    print(instance)

if __name__ == '__main__':
    main()    
