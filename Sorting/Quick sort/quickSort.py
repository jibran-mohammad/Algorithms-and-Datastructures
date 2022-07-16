"""
Implementation of quick sort algorithm.This algorithm sorts elements in ascending order, Its a 
divide and conquer algorithm in which divide step takes O(n) time and conquer steps time depeneds upon the 
partition procedure or how are the elements inside the array arranged. In worst case the partition procedure 
divides the array in two subarray, one of size (n-1) and another of size 0, thus time complexity in worst case 
would be O(n ^ 2). In best and average case, the the parition procedure divides the array into two almost 
equal halves giving the time complexity of O(n log n).
"""
class QuickSort:
    """
    QuickSort class defining two dunder methods __init__ and __str__ and two methods sort and partition used 
    in quick sort.
    """
    def __init__(self, array: list):
        self.array = array
        self.length = len(array)
        self.initialIndex = 0
        self.lastIndex = self.length - 1

    def sort(self, p: int, r: int):
        """
        Recursive sort procedure, which divides the array into two parts, size of those parts depend on 
        another proceudre called partition. This partition procudure depends on arrangement of elements 
        inside the array
        """
        if p < r:
            q = self.partition(p,r)
            self.sort(p, q - 1)
            self.sort(q + 1, r)

    def partition(self, p: int, r: int) -> int:
        """
        This method scans the array from p to r, and at every point checks whether the element at jth location
        is less than or equal to the pivot element, if it is, it's going to increment i and swap it with 
        jth location element. At the end we will have an array which contains a pivot such that the elements
        on the left of pivot are less than or equal to pivot and elements on the right of pivot are greater 
        than pivot 
        """
        pivot = self.array[r]
        i = p - 1
        for j in range(p, r):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i+1], self.array[r] = self.array[r] , self.array[i + 1]
        return i + 1                

    def __str__(self):
        return 'The array is sorted order is %s' % self.array

def main():
    instance = QuickSort([13,19,9,5,12,8,7,4,21,2,6,11])
    instance.sort(instance.initialIndex, instance.lastIndex)
    print(instance)

if __name__ == '__main__':
    main()    