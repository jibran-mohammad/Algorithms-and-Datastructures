"""
Finding the subarray of size k with greatest sum and returning the sum. The time complexity of this algorithm is 
O(n) and space complexity is O(1).The technique used is sliding window
"""
class MaximumSubarraySum:
    def __init__(self, array: list, subarraySize: int):
        self.array = array
        self.subarraySize = subarraySize
        self.windowStart = 0
        self.windowEnd = None
        self.windowSum = 0
        self.maxSum = 0

    def findMaxSum(self):
        for self.windowEnd in range(len(self.array)):
            self.windowSum += self.array[self.windowEnd]
            if self.windowEnd >= self.subarraySize-1:
                if self.maxSum < self.windowSum:
                    self.maxSum = self.windowSum
                self.windowSum -= self.array[self.windowStart]
                self.windowStart += 1

    def __repr__(self):
        return 'The maximum subarray sum of size %d is %d' % (self.subarraySize, self.maxSum)

def main():
    instance = MaximumSubarraySum([2, 1, 5, 1, 3, 2], 3)
    instance.findMaxSum()
    print(instance)

if __name__ == '__main__':
    main()                        