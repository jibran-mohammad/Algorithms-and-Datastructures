

class HeapSort:
    def __init__(self, sequence):
        self.sequence = sequence
        self.heapSize = 0

    def maxHeapifyRecurse(self, i):
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
        self.heapSize = len(self.sequence)
        for i in range((len(self.sequence) // 2) - 1, -1, -1):
            self.maxHeapifyRecurse(i) 
           
    
    def sort(self):
        self.buildMaxHeap()
        for i in range(len(self.sequence) - 1, 0, -1):
            self.sequence[i], self.sequence[0] = self.sequence[0], self.sequence[i]
            self.heapSize = self.heapSize - 1
            self.maxHeapifyRecurse(0)      
    
    def __str__(self):
        return 'Sorted Sequence is: %s' % self.sequence

if __name__== '__main__':
    instance = HeapSort([27,17,3,16,13,10,1,5,7,12,4,8,9,0])
    instance.sort()
    print(instance)            