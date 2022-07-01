"""
Linear Search using recursion
"""

class LinearSearch:
	"""
	Linear Search class containing a recursive function search and __init__ for instance attribute assignment
	and __repr__ for overloading print if instance appears in print 
	"""
    def __init__(self, sequence: list, value: int):
        self.sequence = sequence
        self.length = len(sequence)
        self.value = value
        self.index = None
    

    def search(self, i: int):
    	"""
    	Recursive search function which checks whether the value passed is in the array or not.
    	"""
        if i == self.length - 1:
            return 
        else:
            if self.sequence[i] == self.value:
            	self.index = i
            else:
                i += 1
                self.search(i)
    

    def __repr__(self):
        if self.index == None:
            return 'Element not found'
        else:
            return 'Element found at index %d' % self.index

def main():
	"""
	main function creating instances of class Linear search and passing the value for testing.
	"""
    instance = LinearSearch([1,5,9,33,45,90,2,34,63],9)
    instance.search(0)
    print(instance)
    instance2 = LinearSearch([1,5,6,2,22,64,33,65],90)
    instance.search(0)
    print(instance2)

if __name__ == '__main__':
    main()                                
