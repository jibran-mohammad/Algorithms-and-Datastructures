"""
Merging K sorted lists using min Priority Queue. The algorithm assumes that all the lists are of the same
size. If n will be the total number of elements in the output list and k is the number of lists, then this 
algorithm takes O(nklogk) time
"""

class MergeKSortedLists:
    """
    class MergeKSortedLists contains two operating overloading methods and some other methods like parent,
    leftchild, minheapify, insert etc. The main method used in this class is merge which uses all the 
    methods provided by min Priority queue to perform its task. It maintains a Priority Queue for one element
    in every list, thus the size of priority queue will be the number of lista at maximum. Then it will extract
    min from the priority Queue and then insert the element from the sublist to which min belonged and continue
    until the output list is made.
    """
    def __init__(self, ksortedLists: list[list]):
        self.ksortedLists= ksortedLists
        self.pointers = [0 for array in ksortedLists]
        self.outputArray = [None for j in ksortedLists for i in j]
        self.heapSize = 0
        self.minPriorityHeap = [element[0] for element in ksortedLists]
        self.length= len(self.minPriorityHeap)
        self.lengthOfOneList = len(ksortedLists[0])

    def parent(self, node: int) -> int:
        """
        returns the parent of element at ith index
        """
        return ((node -1) // 2)
    
    def leftChild(self, node: int) -> int:
        """
        returns the left child of node at ith index
        """
        return (2 * node) + 1
    
    def rightChild(self, node: int) -> int:
        """
        returns the parent of element at ith index
        """
        return (2 * node) + 2


    def minHeapify(self,node: int):
        """
        This method takes the index of the node as the argument and assumes the left index node and right index
        node to be the the minHeaps, but the element at ith location might be voilating the minheap
        property, so it moves it downwards in the tree to satisfy the minheap property. If after moving it
        one step downward, the new node voilates the minheap property then the method will recurse and 
        perform the same method again. This procedure takes O(logn) time in worst case.
        """
        l = self.leftChild(node)
        r = self.rightChild(node)
        if l <= self.heapSize and self.minPriorityHeap[l] < self.minPriorityHeap[node]:
            smallest = l
        else:
            smallest = node
        if r <= self.heapSize and self.minPriorityHeap[r] < self.minPriorityHeap[smallest]:
            smallest = r

        if smallest != node:
            self.minPriorityHeap[node], self.minPriorityHeap[smallest] = self.minPriorityHeap[smallest], self.minPriorityHeap[node]
            self.minHeapify(smallest)

    def buildHeap(self):
        """
        Convert the array which isn't a minheap into the minheap. The loop starts from the last nonleaf node
        and starts running minheapify procedure on the element. This procedure takes O(n) time.
        """
        self.heapSize = self.length - 1
        for nonLeaf in range((self.length // 2) - 1, -1, -1):
            self.minHeapify(nonLeaf)
    
    def extractMin(self) -> int:
        """
        return and deletes the minimum priority element in the heap
        """
        minimum = self.minPriorityHeap[0]
        self.minPriorityHeap[0], self.minPriorityHeap[self.heapSize] = self.minPriorityHeap[self.heapSize], self.minPriorityHeap[0]
        self.heapSize -= 1
        self.minHeapify(0)
        return minimum

    def insert(self, key: int):
        """
        Inserts the element inside the max Priority Queue
        """
        self.heapSize += 1
        self.minPriorityHeap[self.heapSize] = float('inf')
        self.decreaseKey(self.heapSize, key)

    def decreaseKey(self, node: int, key: int):
        """
        Decreases the element by the given value
        """
        self.minPriorityHeap[node] = key
        while node > 0 and self.minPriorityHeap[self.parent(node)] > self.minPriorityHeap[node]:
            self.minPriorityHeap[self.parent(node)], self.minPriorityHeap[node] = self.minPriorityHeap[node], self.minPriorityHeap[self.parent(node)]
            node = self.parent(node)    

    def merge(self):
        """
        This method first builds the minheap, then extracts the min from priority queue and then assign it 
        to the output array, then checks which sublists the min belongs to, after finding it, it will insert 
        next element from that sublist to the priority queue. This procedure is followed n times, if the 
        number of elements in the output array is n
        """
        self.buildHeap()
        for i in range(len(self.outputArray)):
            minimum = self.extractMin()
            self.outputArray[i] = minimum
            for k in range(len(self.pointers)):
                if minimum == self.ksortedLists[k][self.pointers[k]]:
                    
                    if self.pointers[k] == self.lengthOfOneList-1:
                        continue
                    else:    
                        self.pointers[k] += 1    
                        self.insert(self.ksortedLists[k][self.pointers[k]])
                        break

    def __str__(self):
        
        return 'The output from merging %s sorted lists is %s' % (self.length, self.outputArray)                

def main():
    instance = MergeKSortedLists([[1,8,4,100], [64,98,200,204], [2,5,9,48]])
    instance.merge()
    print(instance)

if __name__ == '__main__':
    main()    
