"""
Linear search: comparing the element given with every element of array from left to right
returning the index of the element if it's present in the array
otherwise returning None
"""

class LinearSearch:
    """
    class for linear search containg methods like search and some operating overloading methods
    """

    def __init__(self, sequence: list, value: int):
        self.sequence = sequence
        self.value = value
        self.index = None

    def search(self):
        for i in range(0, len(self.sequence)):
            if self.sequence[i] ==  self.value:
                self.index = i
                break
    
    def __repr__(self):
        if self.index == None:
            return 'The value cannot be found in the list'
        else:
            return 'The index of the given value in the list is %d' % self.index

def main():
    instance = LinearSearch([5,6,2,63,9,3,21,60,43,4], 2)
    instance.search()
    print(instance)
    instance2 = LinearSearch([4,3,89,33,78,45,11,3],60)
    instance2.search()
    print(instance2)    
if __name__ == '__main__':
    main()
