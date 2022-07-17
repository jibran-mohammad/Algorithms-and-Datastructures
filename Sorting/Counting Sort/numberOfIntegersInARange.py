"""
Given the number of integers between 0 and k, this algorithm is going to find how many elements fall in the 
range of a to b including a and b. The algorithm runs in O(n + K) time if n is the number of elements present
and k is the range of those elements. If k is O(n), the algorithm runs in O(n) time.
"""

class NumberOfIntegersInARange:
    def __init__(self, array: list, firstNumber: int, secondNumber: int):
        self.array = array
        self.length = len(self.array)
        self.temporaryArray = [0 for i in range(max(self.array) + 1)]
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
        self.numberOfIntegers = 0

    def preprocessing(self):
        for i in range(self.length):
            self.temporaryArray[self.array[i]] += 1
        for i in range(1, len(self.temporaryArray)):
            self.temporaryArray[i] = self.temporaryArray[i] + self.temporaryArray[i - 1]

    def findNumberOfIntegers(self):
        self.numberOfIntegers= self.temporaryArray[self.secondNumber] - self.temporaryArray[self.firstNumber - 1]

    def __str__(self):
        return f'The number of integers between {self.firstNumber} and {self.secondNumber} is {self.numberOfIntegers}'


def main():
    instance = NumberOfIntegersInARange([2,5,3,0,2,3,0,3], 2, 5)
    instance.preprocessing()
    instance.findNumberOfIntegers()
    instance.findNumberOfIntegers() 
    print(instance)
 
if __name__ == '__main__':
    main()           

                    