"""
Implementation of the min Priority Queue. It supports operations heapMin, heapdecreasekey, Insert and 
extract min. This implementation uses minHeap. heapMin will take O(1) time, heapdecreasekey will take
O(logn) time, Insert will take O(logn) time and extract min will take O(logn) time.
"""

class MinPriorityQueue:
    """
    class defined for min Priority Queue with two operating overloading methods and other methods for opearations
    of maipriorityQueue and some support methods like minHeapify, parent, leftchild etc    
    """
    def __init__(self, sequence):
        self.sequence = sequence
        self.heapSize = 0
        self.length = len(sequence)

    def leftChild(self, i):
        """
        returns the left child of node at ith index
        """
        return (2 * i) + 1

    def rightChild(self, i):
        """
        returns the right child of node at ith index
        """
        return (2 * i) + 2

    def parent(self, i):
        """
        returns the parent of element at ith index
        """
        return ((i - 1) // 2)
    
    def minHeapify(self,i):
        """
        This method takes the index of the node as the argument and assumes the left index node and right index
        node to be the the minHeaps, but the element at ith location might be voilating the minheap
        property, so it moves it downwards in the tree to satisfy the minheap property. If after moving it
        one step downward, the new node voilates the minheap property then the method will recurse and 
        perform the same method again. This procedure takes O(logn) time in worst case.
        """
        left = self.leftChild(i)
        right = self.rightChild(i)

        if left <= self.heapSize and self.sequence[left] < self.sequence[i]:
           smallest = left 
        else:
            smallest = i 

        if right <= self.heapSize and self.sequence[right] < self.sequence[smallest]:
            smallest = right 

        if smallest != i:
            self.sequence[smallest], self.sequence[i] = self.sequence[i], self.sequence[smallest]
            self.minHeapify(smallest)                      
    
    def buildMinHeap(self):
        """
        Convert the array which isn't a minheap into the minheap. The loop starts from the last nonleaf node
        and starts running minheapify procedure on the element. This procedure takes O(n) time.
        """
        self.heapSize = self.length - 1
        for j in range((self.length // 2) - 1, -1, -1):
            self.minHeapify(j)

    def __str__(self):
        tempList = []
        for index in range(0, self.heapSize + 1):
                tempList.append(self.sequence[index])
        tempList = [str(x) for x in tempList]        
        return ' '.join(tempList)

    def extractMin(self):
        """
        return and deletes the minimum priority element in the heap
        """
        if self.heapSize < 0:
            return 'No element present in the heap'
        else:    
            minimum = self.sequence[0]
            self.sequence[0] = self.sequence[self.heapSize]
            self.heapSize -= 1
            self.minHeapify(0)
            return minimum

    def minDecreaseKey(self, i, key):
        """
        Decreases the element by the given value
        """
        if key > self.sequence[i]:
            return 1
        else:
            self.sequence[i] = key 
            while i > 0 and self.sequence[i] < self.sequence[self.parent(i)]:
                self.sequence[self.parent(i)], self.sequence[i] = self.sequence[i], self.sequence[self.parent(i)]
                i = self.parent(i)  
    
    def minHeapInsert(self, key):
        """
        Inserts the element inside the max Priority Queue
        """
        self.heapSize = self.heapSize + 1
        self.sequence.append(float('inf'))
        self.minDecreaseKey(self.heapSize, key)

    def delete(self, i):
        """
        Deletes the element at node i
        """
        self.minDecreaseKey(i, float('-inf'))
        self.sequence[0], self.sequence[self.heapSize] = self.sequence[self.heapSize], self.sequence[0]
        self.heapSize -= 1
        self.minHeapify(0)

def main():
    instance = MinPriorityQueue([4,1,3,2,16,9,10,14,8,7])
    instance.buildMinHeap()
    print(instance)
    minimum = instance.extractMin()
    if isinstance(minimum, str):
        print(minimum)
    else:
        print('The min Queue after deleting min element is ')
        print(instance)
    flag = instance.minDecreaseKey(5,0)
    if flag == 1:
        print('The value you want to insert is greater than the value already present at node')
    else: 
        print('The min Priority Queue after decreasing a key by certain value is ')   
        print(instance)
    instance.minHeapInsert(6)
    print("The min Priority Queue after inserting a key is")
    print(instance)
    instance.delete(4)
    print('The sequence after deleting the an element is ', instance)

if __name__=='__main__':
   main() 