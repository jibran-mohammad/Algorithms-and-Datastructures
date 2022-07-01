
import math
class MaximumSubarray:
    def __init__(self, array):
        self.array = array 

    def findMaximumCrossingSubarray(self, low, mid, high):
        leftSum = -100000000000000
        sum = 0
        for i in range(mid,low-1,-1):
            sum += self.array[i]
            if sum > leftSum:
                leftSum = sum 
                maxLeft = i
        rightSum = -100000000000000
        sum = 0
        for j in range(mid+1,high+1):
            sum = sum + self.array[j]
            if sum > rightSum:
                rightSum = sum 
                maxRight = j
        return maxLeft, maxRight, leftSum + rightSum

    def findMaximumSubarray(self, low, high):
        if low == high:
           return low, high, self.array[low]
        else:
            mid = math.floor((low + high)/2)
            leftLow, leftHigh, leftSum = self.findMaximumSubarray(low, mid)
            rightLow, rightHigh, rightSum = self.findMaximumSubarray(mid+1, high)
            crossLow, crossHigh, crossSum = self.findMaximumCrossingSubarray(low, mid, high)
            if leftSum >= rightSum and leftSum >= crossSum:
                return leftLow, leftHigh, leftSum
            elif rightSum >= leftSum and rightSum >= crossSum:
                return rightLow, rightHigh, rightSum
            else:
                return crossLow, crossHigh, crossSum 
                             

if __name__ == '__main__':
    instance = MaximumSubarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7])
    low, high, sum = instance.findMaximumSubarray(0,15)
    print('low=', low, 'high=',high, 'sum=',sum)
