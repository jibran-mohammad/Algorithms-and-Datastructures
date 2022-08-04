"""
Finding Maximum sum subarray from all subarrays of array having length n. The algorithm used is called 
kadan's algorithm and it's based on sliding window technique. The algorithm has the time complexity of 
O(n) and space complexity of O(1)
"""

class MaximumSum:
    """
    MaximumSum class containing two operating overloading methods, __init__() used for creating the attributes 
    of instance and __repr__ used if instance appears in the printing context. It also contains a method
    which does the real work of finding the maximum sum subarray
    """
    def __init__(self, array: list):
        self.array = array
        self.windowStart = 0
        self.windowEnd = None
        self.windowSum = 0
        self.maximumSum = float('-inf')
        self.left = None
        self.right = None

    def findMaximumSum(self):
        for self.windowEnd in range(len(self.array)):
            self.windowSum += self.array[self.windowEnd]
            if self.windowSum > self.maximumSum:
                self.maximumSum = self.windowSum
                self.left = self.windowStart
                self.right = self.windowEnd   
            if self.windowSum < 0:
                self.windowSum = 0
                self.windowStart += 1

    def __repr__(self):
        return ('Maximum subarray in the array %s is %s and its sum is %d' %
                                         (self.array, self.array[self.left:self.right + 1], self.maximumSum))

def main():
    instance = MaximumSum([-2,-5,6,-2,-3,1,5,-6]) 
    instance.findMaximumSum()
    print(instance)

if __name__ =='__main__':
    main()                                                            