"""
Implementation of heap sort, This algorithm sorts the elements in-place i.e at max a constant number
of elements are stored outside an array. It uses heap datastructure for storing the elements. The time 
complexity of this algorithm is O(nlogn) and space complexity is O(1) 
"""

class HeapSort:
    """
    HeapSort class defining the operating overloading method __init__ for initialiazation of instance
    attributes like heapSize, length and sequence of elements. __str__ method which is called if the
    instance of this class appears in printing context and some other methods like maxheapifyRecurse, 
    buildMaxHeap and sort
    """
    def __init__(self, sequence):
        self.sequence = sequence
        self.heapSize = 0
        self.length= len(sequence)

    def maxHeapifyRecurse(self, i):
        """
        This method takes the index of the node as the argument and assumes the left index node and right index
        node to be the the maxHeaps, but the element at ith location might be voilating the maxheap
        property, so it moves it downwards in the tree to satisfy the maxheap property. If after moving it
        one step downward, the new node voilates the maxheap property then the method will recurese and 
        perform the same method again. This procedure takes O(logn) time in worst case.
        """
        l = (2 * i) + 1
        r = (2 * i) + 2
        
        if l < self.heapSize and self.sequence[l] > self.sequence[i]:
            largest = l
        else:
            largest = i
        
        if r < self.heapSize and self.sequence[r] > self.sequence[largest]:
            largest = r 

        if largest != i:
            self.sequence[i], self.sequence[largest] = self.sequence[largest], self.sequence[i]
            self.maxHeapifyRecurse(largest)

    def buildMaxHeap(self):
        """
        Convert the array which isn't a maxheap into the maxheap. The loop starts from the last nonleaf node
        and starts running maxheapify procedure on the element. This procedure takes O(n) time.
        """
        self.heapSize = self.length
        for i in range((len(self.sequence) // 2) - 1, -1, -1):
            self.maxHeapifyRecurse(i) 
           
    
    def sort(self):
        """
        Build the maxheap, then swap the first and last index, decrease the heapsize and apply maxheapify 
        procedure on first element. Perform these operations for every element in an array. This algorithm 
        takes O(nlogn) time.
        """
        self.buildMaxHeap()
        for i in range(self.length - 1, 0, -1):
            self.sequence[i], self.sequence[0] = self.sequence[0], self.sequence[i]
            self.heapSize = self.heapSize - 1
            self.maxHeapifyRecurse(0)      
    
    def __str__(self):
        return 'Sorted Sequence is: %s' % self.sequence

def main():
    instance = HeapSort([27,17,3,16,13,10,1,5,7,12,4,8,9,0])
    instance.sort()
    print(instance)

if __name__== '__main__':
    main()              