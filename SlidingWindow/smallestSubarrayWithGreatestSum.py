"""
Finding the smalllest subarray with sum greater than or equal to k(given sum). The technique used in this 
algorithm is sliding window in which the window size keeps changing. This algorithm will work only for positive
numbers. The time Complexity of this algorithm is O(n), where n is the size of the array.
"""

class SmallestSubarray:
    """
    class SmallestSubarray defining two dundar methods and one other method for calculating the smallest
    subarray with sum greater than given sum
    """
    def __init__(self, array: list, givenSum: int):
        self.array = array 
        self.length = len(array)
        self.windowStart = 0
        self.windowEnd = 0
        self.minLength = float('inf')
        self.windowSum = 0
        self.outputSum = None
        self.sum = givenSum
        self.left = None
        self.right = None

    def findSmallestSubarray(self):
        """
        First we will keep adding the size of the window until it reaches a point where the sum of window
        will be greater than or equal to given sum. Then we will calculate the length of the window and store it
        in minLength, after that we will keep decreasing the size of window from windowStart and calculating the
        new windowSum, if new WindowSum is greater then or equal to given sum, then change the min length
        and store the coordinates of the window and repeat the process until window sum will be less than
        given sum.Repeat the process until you reach the end.
        """
        for self.windowEnd in range(self.length):
            self.windowSum += self.array[self.windowEnd]
            
            if self.windowSum >= self.sum:
                while self.windowSum >= self.sum:
                    if self.minLength > (self.windowEnd - self.windowStart) + 1:
                        self.left = self.windowStart
                        self.right = self.windowEnd
                        self.outputSum = self.windowSum  
                    self.minLength = min(self.minLength, (self.windowEnd - self.windowStart) + 1)
                    self.windowSum -= self.array[self.windowStart]
                    self.windowStart += 1

    def __repr__(self):
        return f'Minimum length subarray with sum greater then {self.sum} starts at {self.left} and ends at {self.right} with sum as {self.outputSum}'


def main():
   instance = SmallestSubarray( [2, 1, 5, 2, 3, 2], 8)
   instance.findSmallestSubarray()
   print(instance)         

if __name__ == '__main__':
    main()   