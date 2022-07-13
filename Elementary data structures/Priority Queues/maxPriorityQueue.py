
import sys

class MaxPriorityQueue:
    def __init__(self, sequence):
        self.sequence = sequence
        self.heapSize = 0
    
    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return (2 * i) + 1

    def rightChild(self,i):
        return (2 * i) + 2

    def maxHeapify(self, i):
        left = self.leftChild(i)
        right = self.rightChild(i)

        if left < self.heapSize and self.sequence[left] > self.sequence[i]:
            largest = left
        else:
            largest = i 

        if right < self.heapSize and self.sequence[right] > self.sequence[largest]:
            largest = right

        if largest != i:
            self.sequence[i], self.sequence[largest] = self.sequence[largest], self.sequence[i]
            self.maxHeapify(largest)

    def buildHeap(self):
        self.heapSize = len(self.sequence)
        for i in range((len(self.sequence) // 2) -1, -1, -1):
            self.maxHeapify(i) 

    def heapMax(self):
        return self.sequence[0]

    def heapExtractMax(self):
        if self.heapSize < 0:
            print('No element present in the heap')

        max = self.sequence[0]
        self.sequence[0] = self.sequence[self.heapSize - 1]
        self.heapSize = self.heapSize - 1
        self.maxHeapify(0) 
        return max 

    def heapIncreaseKey(self, i, key):
        if key < self.sequence[i]:
            print('New key is smaller than the current value')
            return
        self.sequence[i] = key 

        while i > 0 and self.sequence[i] >= self.sequence[self.parent(i)]:
            self.sequence[i], self.sequence[self.parent(i)] = self.sequence[self.parent(i)], self.sequence[i]
            i = self.parent(i)

    def maxHeapInsert(self, key):
        minsize = -sys.maxsize - 1
        self.heapSize += 1
        self.sequence.append(minsize)
        self.heapIncreaseKey(self.heapSize - 1, key)
    
    def __str__(self):
        tempList = []
        i = 0
        for x in self.sequence:
            if i < self.heapSize:
                tempList.append(x)
                i += 1
        return 'Sequence is: %s' % tempList


if __name__ == '__main__':
    instance = MaxPriorityQueue([15,13,9,5,12,8,7,4,0,6,2,1])
    instance.buildHeap()
    maximum = instance.heapExtractMax()
    print('The maximum number extracted is:', maximum)
    print('After extracting max, the resulted sequence is')
    print(instance)
    maximum = instance.heapMax()
    print('The maximum element in the heap is: ', maximum)
    instance.heapIncreaseKey(3, 100)
    print('The sequence after key at location 3 has been incresed is:', instance)
    instance.maxHeapInsert(25)
    print('The sequence after insertion took place is: ', instance)

