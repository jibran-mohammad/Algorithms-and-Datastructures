"""
The implementation of the algorithm for finding the ith smallest element in an array. This algorithm uses a
partition procedure like quicksort but it enforces the condition that the pivot element is choosen randomly, 
which will enable us to use probabilistic analysis to find the average expected time of the algorithm. The 
expected running time of this algorithm is O(n). Unlike quicksort, this algorithm calls the recursive procedure
for either one of the partition not the both.
"""

import random 
class IthSmallestElement:
    """
    class IthSmallestElement defining one dundar method and other methods like randomizedPartition, partition
    and randomized Select.
    """
    def __init__(self, array: list, i: int):
        self.array = array
        self.length = len(array)
        self.left = 0
        self.right = self.length - 1
        self.i = i 

    def randomizedPartition(self, left: int , right: int)-> int:
        """
        This method ensures that the pivot element is choosen randomly by using randint psuedo random number 
        generator. After that the random element we got from random index is swapped with the last element, 
        because our partition procedure is dependent on using last element as pivot element.
        """
        randomIndex = random.randint(left, right) 
       
        self.array[randomIndex], self.array[right] = self.array[right], self.array[randomIndex]
        
        mid = self.partition(left, right)
        
        return mid

    def partition(self, left: int, right: int) -> int:
        """
        This method first calculates the ith index, it represents an index which says the elements to the left 
        of index i are less than or equal to pivot at every point that is why initially i is assigned to left -1
        which means i is outside the array initially. J scans the array from left to right - 1 and if anytime
        it if found that element at j is less than or equal to pivot, we increment i and swap ith and jth element
        At last we swap i+1th element with pivot and return i + 1 which will be mid point.
        """
        i = left - 1
        pivot = self.array[right]
        
        for j in range(left, right):
            if self.array[j] <= pivot:
                i +=1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        
        self.array[right], self.array[i + 1] = self.array[i + 1], self.array[right]

        return i + 1

    def randomizedSelect(self, left: int, right: int, i: int) -> int:
        """
        In this method we are going to check whether left and right are equal, if they are then element at that
        index is the ith smallest, this case will occur only when i = 1. Then we partition the array and calculate
        the mid point. After that we calculate the elements of the left array of partition, including pivot, because
        we need to find whether ith element is the pivot or is it in the left array or right array. That is 
        why we check the condition whether the ith element is pivot, if it is, then we return it, if i is less 
        than number of elements in left array, it means ith smallest element will be present in left array,
        otherwise it would be present in the right array, when we call the right array we decrement i by 
        Number of elements found in left array, because if ith element is in the right array, we have already
        found the number of elements in left array which will be smaller than i.
        """
        if left == right:
            return self.array[left]
        mid = self.randomizedPartition(left, right)
        
        elementCountLeftArray = mid - left + 1 

        if i == elementCountLeftArray:
            return self.array[mid]
        elif i < elementCountLeftArray:
            return self.randomizedSelect(left, mid - 1, i)
        else:
            return self.randomizedSelect(mid + 1, right, i - elementCountLeftArray)

def main():
    instance = IthSmallestElement([3,2,9,0,7,5,4,8,6,1], 5)
    element= instance.randomizedSelect(instance.left, instance.right, instance.i)
    print(f'The {instance.i}th smallest element is {element}')

if __name__ == '__main__':
    main()    

                      