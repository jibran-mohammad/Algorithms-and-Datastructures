"""
Insertion sort sorting numbers in decreasing order. Time complexity is O(n ^ 2 ) where n is the size of the 
array
"""

class InsertionSort:
    """
    A class of Insetion sort with methods sort and some operator overloading methods
    """
    
    def __init__(self, sequence:list):
        self.sequence = sequence

    def sort(self):
        """
        sort method which compares the key with elements of subarray which is on the left side of key until its 
        proper location is found
        """
        for j in range(1,len(self.sequence)):
            key = self.sequence[j]
            i = j - 1
            while i >= 0 and key > self.sequence[i]:
                self.sequence[i+1] = self.sequence[i]
                i -= 1
            self.sequence[i + 1] = key
    
    def __str__(self):
        return 'Sorted sequence is %s' % self.sequence

def main():
    instance = InsertionSort([1,2,6,34,56,22,12,0])
    instance.sort()
    print(instance)         

if __name__ == '__main__':
    main()                  