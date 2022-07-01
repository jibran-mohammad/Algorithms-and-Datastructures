
import sys
class MinPriorityQueue:
    def __init__(self, sequence):
        self.sequence = sequence
        self.heapSize = 0

    def leftChild(self, i):
        return (2 * i) + 1

    def rightChild(self, i):
        return (2 * i) + 2

    def parent(self, i):
        return ((i - 1) // 2)
    
    def minHeapify(self,i):
        left = self.leftChild(i)
        right = self.rightChild(i)

        if left < self.heapSize and self.sequence[left] < self.sequence[i]:
           smallest = left 
        else:
            smallest = i 

        if right < self.heapSize and self.sequence[right] < self.sequence[smallest]:
            smallest = right 

        if smallest != i:
            self.sequence[smallest], self.sequence[i] = self.sequence[i], self.sequence[smallest]
            self.minHeapify(smallest)                      
    
    def buildMinHeap(self):
        self.heapSize = len(self.sequence)
        n = len(self.sequence)
        for j in range((n // 2) - 1, -1, -1):
            self.minHeapify(j)

    def __str__(self):
        tempList = []
        j = 0
        for x in self.sequence:
            if j < self.heapSize:
                tempList.append(x)
                j += 1
        return 'Sequence is: %s' % tempList

    def extractMin(self):
        minimum = self.sequence[0]
        self.sequence[0] = self.sequence[self.heapSize - 1]
        self.heapSize -= 1

        self.minHeapify(0)

    def minDecreaseKey(self, i, key):
        if key > self.sequence[i]:
            print('Key given is larger than the key present')
            return 
        
        self.sequence[i] = key 
        while i > 0 and self.sequence[i] < self.sequence[self.parent(i)]:
            self.sequence[self.parent(i)], self.sequence[i] = self.sequence[i], self.sequence[self.parent(i)]
            i = self.parent(i)  
    
    def minHeapInsert(self, key):
        self.heapSize = self.heapSize + 1
        self.sequence.append(sys.maxsize)
        self.sequence[self.heapSize]= sys.maxsize
        self.minDecreaseKey(self.heapSize, key)

if __name__=='__main__':
    instance = MinPriorityQueue([15,13,9,5,12,8,7,4,0,6,2,1])
    instance.buildMinHeap()
    print(instance)
    instance.extractMin()
    print(instance)
    instance.minDecreaseKey(5,0)
    print(instance)
    instance.minHeapInsert(6)
    print(instance)