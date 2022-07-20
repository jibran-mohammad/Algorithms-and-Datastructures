"""
Problem: Given an array containing only zeros and ones, sort the array such that the sort algorithm runs in 
O(n) time and the algorithm is stable.
"""

class ZerosAndOnesArraySort:
    def __init__(self, inputArray: list):
        self.inputArray = inputArray
        self.length = len(inputArray)
        self.outputArray = [None for i in range(self.length) ]

    def sort(self):
        indexOutputArray = 0
        
        for index1 in range(self.length):
            if self.inputArray[index1] == 0:
                self.outputArray[indexOutputArray] = 0
                indexOutputArray += 1

        for index2 in range(self.length):
            if self.inputArray[index2] == 1:
                self.outputArray[indexOutputArray] = 1
                indexOutputArray += 1

    def __str__(self):
        return f'The Array containing only zeros and ones in stable sorted order is {self.outputArray}'

def main():
    instance = ZerosAndOnesArraySort([1,0,1,1,0,0,1,0,1,0])
    instance.sort()
    print(instance)

if __name__ == '__main__':
    main()                                    