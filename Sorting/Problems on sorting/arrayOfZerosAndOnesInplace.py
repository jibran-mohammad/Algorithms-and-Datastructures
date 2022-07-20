"""
Problem: Given the array of zeros and ones, sort the array so that the algorithm takes O(n) time to sort and 
sort the array in place. It can or cannot be stable.
"""

class ZerosAndOnesSort:
    def __init__(self, array: list):
        self.array = array
        self.length = len(array)

    def sort(self):
        """
        variable index is created which is going to represent number of zeros seen so far, so if the number 
        of zeros inside an array is x, then index would range from 0 to x-1. Then we iterate every element
        of an array and every time we encounter the elemnent with zero value we swap it with the element at
        indices given by index, because 0 encountered anywhere will be in the range of index variable.
        """
        index = 0

        for index1 in range(self.length):
            if self.array[index1] == 0:
                self.array[index1] , self.array[index] = self.array[index], self.array[index1]
                index += 1

    def __repr__(self):
        return f"The array containing only zeros and ones in sorted order is {self.array}"

def main():
    instance = ZerosAndOnesSort([0,1,1,1,0,0,1,0,0,1,1,0])
    instance.sort()
    print(instance)

if __name__ == '__main__':
    main()            