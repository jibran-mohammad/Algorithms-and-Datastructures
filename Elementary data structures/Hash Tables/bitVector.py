"""
implementation of a bit vector which is basically an array of 0's and 1's. We are representing a dynamic set
using bit vector with distinct elements and with no satellite data. If the key is present, it's location will
contain 1, otherwise it will contain 0. Delete will make a particular location 0 given by key and search will
return either True or False, depending upon whether element with particular key is present or not. All operations
will take O(1) time
"""
class BitVector:
    """
    class BitVector defining two dundar methods and three other methods named insert, delete and search.
    """
    def __init__(self, size: int):
        self.array = [0 for i in range(size)]
        self.length = size

    def insert(self, key: int):
        self.array[key] = 1

    def delete(self, key: int):
        if self.array[key] == 0:
            print('Key isn"t present')
        else:
            self.array[key]= 1

    def search(self, key:int):
        if self.array[key] == 1:
            return True
        else:
            return False

    def __repr__(self):
        return f'The keys which are present are {[key for key in range(self.length) if self.array[key] == 1]}'

def main():
    instance = BitVector(10)
    instance.delete(9)
    instance.insert(3)
    instance.insert(1)
    instance.insert(7)
    instance.insert(8)
    instance.insert(9)
    print(instance)
    result= instance.search(6)
    print(result)
    print(instance)

if __name__== '__main__':
    main()    



