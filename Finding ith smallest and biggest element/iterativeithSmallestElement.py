"""
The implementation of the algorithm for finding the ith smallest element in an array. This algorithm uses a
partition procedure like quicksort but it implements it in iterative manner. The 
expected running time of this algorithm is O(n).
"""

import random
class IthSmallestNumber:
    """
    class IthSmallestElement defining tow dundar methods and other methods like  partition
    and select.
    """
    def __init__(self, array: list, i: int):
        self.array = array
        self.length = len(self.array)
        self.i = i
        self.smallestElement = None
        self.left = 0
        self.right = self.length - 1

    def partition(self, left: int, right: int)-> int:
        """
        This method first calculates the ith index, it represents an index which says the elements to the left 
        of index i are less than or equal to pivot at every point that is why initially i is assigned to left -1
        which means i is outside the array initially. J scans the array from left to right - 1 and if anytime
        it if found that element at j is less than or equal to pivot, we increment i and swap ith and jth element
        At last we swap i+1th element with pivot and return i + 1 which will be mid point.
        """
        pivot = self.array[right]
        index = left - 1

        for j in range(left, right):
            if self.array[j] <= pivot:
                index += 1
                self.array[index], self.array[j] = self.array[j], self.array[index]
        self.array[index + 1], self.array[right] = self.array[right], self.array[index + 1]

        return index + 1
    
    def select(self,left: int, right: int): 
        """
        In this method we are going to check whether left is less than right if it is then the loop statements
        execute. Then we partition the array and calculate the mid point. After that we calculate the elements
        of the left array of partition, including pivot, because we need to find whether ith element is the pivot
        or is it in the left array or right array. That is why we check the condition whether the ith element is
        pivot, if it is, then we assign smallest element to pivit, if i is less than number of elements in left 
        array, it means ith smallest element will be present in left array, otherwise it would be present in the 
        right array, when we change the index for right array we decrement i by Number of elements found in left
        array, because if ith element is in the right array, we have already found the number of elements in 
        left array which will be smaller than i.
        """
        while left < right:
            mid = self.partition(left, right) 
            numberOfElementsLeftArray = mid - left + 1 

            if numberOfElementsLeftArray == self.i:
               self.smallestElement = self.array[mid]
               break

            if self.i < numberOfElementsLeftArray:
                right = mid - 1
            else:
                left = mid + 1
                self.i = self.i - numberOfElementsLeftArray
        else:        
            self.smallestElement = self.array[left]   
    
    def __repr__(self):
        return f"The {self.i}th smallest element in the array is {self.smallestElement}"

def main():
    instance = IthSmallestNumber([5,4,83,72,16,0,3,24], 3) 
    instance.select(instance.left, instance.right)
    print(instance)

if __name__ == '__main__':
    main()                            
