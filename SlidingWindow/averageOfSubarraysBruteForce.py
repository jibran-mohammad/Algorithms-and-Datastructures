"""
Finding the average of all subarrays of size k of the given array. This algorithm used brute force technique
and the time complexity of the algorithm is O(n * k) where n is the length of subarray and k is the size of 
subarrays we want to find average of 
"""

class AverageOfSubarrays:
     """
     Class AverageOfSubarrays defining __init__ operator overloading method for creating the instance attributes,
     __repr__ operating overloading method for redirecting the control to this method if instance appears
     in printing context and findAverageOfSubarrays method for actually calculating the result.
     """
     def __init__(self, array: list, k: int):
         self.array = array 
         self.size = k
         self.indices = len(array) - k + 1
         self.result = []

     def findAverageOfSubarrays(self):
         for i in range(self.indices):
             _sum = 0.0
             for j in range(i, i + self.size):
                 _sum = _sum + self.array[j]
             self.result.append(_sum/self.size)

     def __repr__(self):
         return 'The average of all subarrays of size %d of array %s is %s' % (self.size, self.array, self.result)

def main():
    instance = AverageOfSubarrays([1,3,2,6,-1,4,1,8,2],5)
    instance.findAverageOfSubarrays()
    print(instance)

if __name__ == '__main__':
    main()    

