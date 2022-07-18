"""
This is the implementation of counting sort. It creates a temporaray array of size k and the input array is of
size n. The time complexity would be O(n) if k is O(n). It's a stable version of counting sort algorithm which
means if there are elements inside the array with same value, it will store them in output array in the same 
order, the order they were in original array, although that only makes sense, if there is a satellite data
associated with the elements. The space complexity is also O(n+k) and if k = O(n), the space complexity is
O(n).
"""

class CountingSort:
    """
    class Countingsort defing two operating overloading methods and one sort method
    """
    def __init__(self, array: list):
        self.array = array
        self.length = len(array)
        self.outputArray = [None for i in range(self.length)]
        self.temporaryArray = [0 for i in range(max(self.array) + 1)]

    def sort(self):
        """
        The temporary indices represent the element in original array, and first we run for loop to see how 
        many such elemnts are present in the original array. Then for every element in the orginal array 
        we see how many elements are in less than or equal to the given element which will give the location
        of that element in the output array.
        """
        for i in range(self.length):
            self.temporaryArray[self.array[i]] = self.temporaryArray[self.array[i]] + 1
        for i in range(1, len(self.temporaryArray)):
            self.temporaryArray[i] = self.temporaryArray[i] + self.temporaryArray[i - 1]
        for i in range(self.length - 1, -1, -1):
            self.outputArray[self.temporaryArray[self.array[i]] - 1] = self.array[i]
            self.temporaryArray[self.array[i]] -= 1

    def __str__(self):
        return  f'The sorted array is {self.outputArray}'

def main():
    instance = CountingSort([2,5,3,0,2,3,0,3])
    instance.sort()
    print(instance)

if __name__ == '__main__':
    main()                    
            
                        