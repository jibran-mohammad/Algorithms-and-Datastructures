"""
Implementation of Bubble Sort. Time complexity of this algorthim is going to be O(n^2)
"""

class BubbleSort:
    """
    class BubbleSort defining two operating overloading methods and a sort method.
    """
    def __init__(self, array: list):
        self.array = array
        self.length = len(array)

    def sort(self):
        """
        The first for loop run's n-1 times, if n is the number of elements in the array, the second for loop 
        first runs for n-1, then n-2, then n-3 and it continues till 0. At every iteration the element at the 
        index2 and index2 + 1 is compared, if element at index2 is greater than element at index2 + 1, then 
        those elements are swapped, this process will repeat for n-1 times and in the firt pass, greatest 
        element will be at the last which is its correct position.Then next pass will  start and process
        continues till n-1 passes.
        """
        leng = self.length - 1
        for index1 in range(self.length - 1):
            for index2 in range(leng):
                if self.array[index2] > self.array[index2 + 1]:
                    self.array[index2], self.array[index2 + 1] = self.array[index2 + 1], self.array[index2]
            leng -= 1
    
    def __str__(self):
        return f'The array is sorted order is {self.array}'

def main():
    instance = BubbleSort([1,4,0,3,9,6,2,34,12,78,33])
    instance.sort()
    print(instance)

if __name__ == '__main__':
    main()                            
