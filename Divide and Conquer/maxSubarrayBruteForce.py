"""
Finding the maximum subarray using brute force: This algorithm takes O(n^2) time. Space complexity is O(1)
"""
class MaximumSubarray:
    """
    A class MaximumSubarray which contains __init__ method for creating attributes of instances and has maxsubarray 
    method which applies brute force for finding all pair of indices of array, finding the sum and then finding
    maximum among them.
    """    
    def __init__(self, array: list):
        self.array = array
        self.maxSum = array[0]
        self.currentSum= 0
        self.left= 0
        self.right= 0 

    def maxSubarray(self):
        n = len(self.array)
        for i in range(n):
            self.currentSum = 0
            for j in range(i,n):
                self.currentSum = self.currentSum + self.array[j]
                if self.currentSum > self.maxSum:
                    self.maxSum = self.currentSum 
                    self.left = i 
                    self.right = j

    def __repr__(self):
        return 'leftIndex= %d, rightIndex= %d, Sum = %d' % (self.left, self.right, self.maxSum)                

def main():
   instance = MaximumSubarray([1, -3, 4, -1, 2, 1, -5, 5])
   instance.maxSubarray()
   print(instance)         
      
if __name__ == "__main__":
    main()
                        