"""
Finding the average sum of subarrays of an array using sliding window technique. The time complexity
of algorithm is O(n) and space complexity is O(1)
"""

class AverageSum:
    """
    Average Sum class containing __init__ operating overloading method for instance attribute creation
    like array, windowStart, windowEnd, size etc. It also defines averageSum method which calculates actual 
    average of subarrays of size k.
    """    
    def __init__(self, array: list, size: int):
        self.array = array
        self.windowStart = 0
        self.windowEnd = None
        self.windowSum = 0.0
        self.size = size
        self.result = []

    def averageSum(self):
        for self.windowEnd in range(len(self.array)):
            self.windowSum += self.array[self.windowEnd]
            if self.windowEnd >= self.size-1:
                self.result.append(self.windowSum / self.size)
                self.windowSum -= self.array[self.windowStart]
                self.windowStart +=1

    def __repr__(self):
        return 'The average sum of subarrays in array %s is %s' % (self.array, self.result)

def main():
    instance = AverageSum([1,3,2,6,-1,4,1,8,2], 5)
    instance.averageSum()
    print(instance)
    instance2 = AverageSum([1,12,-5,-6,50,3], 4)
    instance2.averageSum()
    print(instance2) 

if __name__ == '__main__':
    main()                        