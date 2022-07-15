"""
Implementation of the max Priority Queue. It supports operations heapMax, heapIncreasekey, Insert and 
extract max. This implementation uses maxHeap. heapMax will take O(1) time, heapIncreasekey will take
O(logn) time, Insert will take O(logn) time and extract max will take O(logn) time.
"""

class MaxPriorityQueue:
    """
    class defined for max Priority Queue with two operating overloading methods and other methods for opearations
    of maxpriorityQueue and some support methods like maxHeapify, parent, leftchild etc    
    """
    def __init__(self, sequence:list):
        self.sequence = sequence
        self.length= len(sequence)
        self.heapSize = 0
    
    def parent(self, i:int)-> int:
        """
        returns the parent of element at ith index
        """
        return (i - 1) // 2

    def leftChild(self, i:int)-> int:
        """
        returns the left child of node at ith index
        """
        return (2 * i) + 1

    def rightChild(self,i:int)-> int:
        """
        returns the right child of node at ith index
        """
        return (2 * i) + 2

    def maxHeapify(self, i:int):
        """
        This method takes the index of the node as the argument and assumes the left index node and right index
        node to be the the maxHeaps, but the element at ith location might be voilating the maxheap
        property, so it moves it downwards in the tree to satisfy the maxheap property. If after moving it
        one step downward, the new node voilates the maxheap property then the method will recurse and 
        perform the same method again. This procedure takes O(logn) time in worst case.
        """
        left = self.leftChild(i)
        right = self.rightChild(i)

        if left <= self.heapSize and self.sequence[left] > self.sequence[i]:
            largest = left
        else:
            largest = i 

        if right <= self.heapSize and self.sequence[right] > self.sequence[largest]:
            largest = right

        if largest != i:
            self.sequence[i], self.sequence[largest] = self.sequence[largest], self.sequence[i]
            self.maxHeapify(largest)

    def buildHeap(self):
        """
        Convert the array which isn't a maxheap into the maxheap. The loop starts from the last nonleaf node
        and starts running maxheapify procedure on the element. This procedure takes O(n) time.
        """
        self.heapSize = self.length - 1
        for i in range((self.length // 2) -1, -1, -1):
            self.maxHeapify(i) 

    def heapMax(self):
        """
        return the maximum priority element in the heap
        """
        return self.sequence[0]

    def heapExtractMax(self):
        """
        return and deletes the maximum priority element in the heap
        """
        if self.heapSize < 0:
            return 'No element present in the heap'
        else:
            max = self.sequence[0]
            self.sequence[0] = self.sequence[self.heapSize]
            self.heapSize = self.heapSize - 1
            self.maxHeapify(0) 
            return max 

    def heapIncreaseKey(self, i:int, key:int):
        """
        Increases the element by the given value
        """
        if key < self.sequence[i]:
            return 1
        else:  
            self.sequence[i] = key 

            while i > 0 and self.sequence[i] >= self.sequence[self.parent(i)]:
                self.sequence[i], self.sequence[self.parent(i)] = self.sequence[self.parent(i)], self.sequence[i]
                i = self.parent(i)

    def insert(self, key:int):
        minsize = float('-inf')
        self.heapSize += 1
        self.sequence.append(minsize)
        self.heapIncreaseKey(self.heapSize, key)

    def delete(self, i:int):
        """
        this method deletes the node at ith location. It takes O(logn) time
        """
        self.heapIncreaseKey(i, float('inf'))
        self.sequence[0], self.sequence[self.heapSize] = self.sequence[self.heapSize], self.sequence[0]
        self.heapSize -= 1    
        self.maxHeapify(0)

    def __str__(self):
        tempList = []
        for i in range(0,self.heapSize + 1):
            tempList.append(self.sequence[i])
        tempList = [str(x) for x in tempList]
        return ' '.join(tempList)

def main():
    instance = MaxPriorityQueue([4,1,3,2,16,9,10,14,8,7])
    instance.buildHeap()
    print(instance)
    maximum = instance.heapExtractMax()
    if isinstance(maximum, str):
        print('No element present in the heap')
    else:    
        print('The maximum number extracted is:', maximum)
        print('After extracting max, the resulted sequence is')
        print(instance)
    maximum = instance.heapMax()
    print('The maximum element in the heap is: ', maximum)
    flag = instance.heapIncreaseKey(3, 100)
    if flag ==1:
        print('New key is smaller than the original key')
    else:    
        print('The sequence after key at location 3 has been increased is:', instance)
    instance.insert(25)
    print('The sequence after insertion took place is: ', instance)
    instance.delete(4)
    print('The sequence after the element has been deleted is ', instance)

if __name__ == '__main__':
    main()

