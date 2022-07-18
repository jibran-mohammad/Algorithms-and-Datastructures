"""
Implementation of the radix sort. It uses counting sort internally and the time complexity of this algorithm
is O(d(n + k)). 'k' here is 10, because this algorithm works on positive integers in decimal number format.
It won't work with strings. Thus the time complexity will be O(dn), where d is the number of digits of the max
number and n is the number of elements to be sorted
"""

class RadixSort:
    """
    class RadixSort defining two dunder methods and one sort() and one countingSort() method.
    """
    def __init__(self, inputArray: list):
        self.inputArray = inputArray
        self.length = len(inputArray)
        self.outputArray = [None for i in range(self.length) ]
        maximum = max(self.inputArray)
        temporaryString = str(maximum)
        temporaryList = list(temporaryString)
        self.noOfDigits = len(temporaryList) 
        self.temporaryArray = [0 for i in range(10)]
        
    def sort(self):
        """
        This method starts from the least significant digit and sorts the numbers according to this LSD using
        counting sort, then it works on second last digit and sorts the numbers according to this digit, it 
        continue's till the last digit.
        """
        for count in range(1, self.noOfDigits + 1):
            self.countingSort(count)
            for i in range(self.length):
                self.inputArray[i] = self.outputArray[i]
            for i in range(10):
                self.temporaryArray[i] = 0

    def countingSort(self, count):
        """
        The temporary indices represent the element in original array, and first we run for loop to see how 
        many such elemnts are present in the original array. Then for every element in the orginal array 
        we see how many elements are in less than or equal to the given element which will give the location
        of that element in the output array.
        """
        for indexelement in range(self.length):
            quotient = self.inputArray[indexelement]
            for indexcount in range(count):
                digit = quotient % 10
                quotient = quotient // 10
            self.temporaryArray[digit] += 1

        for indexTemporaryElement in range(1,10):
            self.temporaryArray[indexTemporaryElement] = self.temporaryArray[indexTemporaryElement] + self.temporaryArray[indexTemporaryElement - 1]
        
        for indexOutputElement in range(self.length - 1, -1, -1):
            quotient = self.inputArray[indexOutputElement]
            for indexcount in range(count):
                digit = quotient % 10
                quotient = quotient // 10
               
            self.outputArray[self.temporaryArray[digit] - 1] = self.inputArray[indexOutputElement] 
            self.temporaryArray[digit] -= 1
           
    
    def __str__(self):
        return f'The sorted array is {self.outputArray}'

def main():
    instance = RadixSort([329,774,657,1000,6,83,365])
    instance.sort()
    print(instance)

if __name__ == '__main__':
    main()                       


