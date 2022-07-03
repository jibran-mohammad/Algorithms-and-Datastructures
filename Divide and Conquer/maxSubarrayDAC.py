"""
Finding the subarray inside an array with greatest sum, design technique used is divide and conquer.
Time complexity is O(nlogn) and space complexity is O(logn)
"""
import math

class MaximumSubarray:
    """
    class Named MaximumSubarray.Contains __init__ for instance attribute.Two methods findMaximumCrossingSubarray and findMaximumSubarray
    """

    def __init__(self, array: list):
        self.array = array
        self.low = 0
        self.high = len(array) - 1 
        self.maxLeft = None
        self.maxRight = None
        self.sum = None

    def findMaximumCrossingSubarray(self, low: int, mid: int, high: int) -> tuple:
        """
        This method is going to find the maximum subarray by crossing the mid point. That is
        The left index will be before the mid and the right index will be after the mid. It will divide the 
        array into two halves array[low - mid] and array[mid+1 - high] and will find the maximum subaaray 
        in these subarrays and then combines them
        """

        leftSum = float('-inf')
        sum = 0
        
        # finding the maximum subarray in array[low - mid].leftSum is going to hold the greatest sum 
        # so far and maxLeft is going to hold the index.
        for i in range(mid, low-1, -1):
            sum += self.array[i]
            if sum > leftSum:
                leftSum = sum 
                maximumLeft = i
    
        rightSum = float('-inf')
        sum = 0
        
        # finding the maximum subarray in array[mid+1 - high ].RightSum holds the greatest sum so far 
        # and maxRight will hold the index
        for j in range(mid+1,high+1):
            sum = sum + self.array[j]
            if sum > rightSum:
                rightSum = sum 
                maximumRight = j
    
        return (maximumLeft, maximumRight, (leftSum + rightSum))

    def findMaximumSubarray(self, low: int, high: int):
        if low == high:
           return (low, high, self.array[low])
        else:

            # dividing the array into almost two equal halves
            mid = (low + high) // 2

            # solving two subproblems recursively and one problem with a methods we defined earlier
            (leftLow, leftHigh, leftSum) = self.findMaximumSubarray(low, mid)
            (rightLow, rightHigh, rightSum) = self.findMaximumSubarray(mid+1, high)
            (crossLow, crossHigh, crossSum) = self.findMaximumCrossingSubarray(low, mid, high)
            
            
            # checking which among the three objects holds the maximum sum
            if leftSum >= rightSum and leftSum >= crossSum:
                return leftLow, leftHigh, leftSum
            elif rightSum >= leftSum and rightSum >= crossSum:
                return rightLow, rightHigh, rightSum
            else:
                return crossLow, crossHigh, crossSum 
                
    def assignInstanceAttributes(self, left: int, right: int , Sum: int):
        self.maxLeft = left
        self.maxRight= right
        self.sum = Sum
    
    def __repr__(self):
        return 'low=, %d, high=, %d, sum= %d' % (self.maxLeft, self.maxRight, self.sum)

def main():
    instance = MaximumSubarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7])
    Left, Right, Sum =instance.findMaximumSubarray(instance.low, instance.high)
    instance.assignInstanceAttributes(Left,Right,Sum)
    print(instance)


if __name__ == '__main__':
    main()