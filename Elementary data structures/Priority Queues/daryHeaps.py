"""
Implementation of d-ary heaps, i.e the maximum number of children the node can have is d.
"""

class DArrayHeap:
    """
    Class DArrayHeap provides operating overloading methods like __init__ and __str__, and other methods like
    parent, child, maxHeapify, delete, insert etc
    """
    def __init__(self, array: list, maximumChildren: int):
        self.array = array 
        self.heapSize = 0
        self.length = len(array)
        self.maximumChildren = maximumChildren
        self.lastNonLeafNode = (self.length - 2) // self.maximumChildren

    def parent(self, node:int) -> int:
        """
        returns the parent of element at ith index
        """
        return (node - 1) //  self.maximumChildren

    def child(self, k: int, node:int) -> int:
        """
        return the kth child node at position given by local variable node.
        """
        return (self.maximumChildren * node) - self.maximumChildren + k +3    

    def maxHeapify(self, node: int):
        """
        This method takes the index of the node as the argument and assumes that all subtrees are 
        maxHeaps, but the element at nodeth location might be voilating the maxheap
        property, so it moves it downwards in the tree to satisfy the maxheap property. If after moving it
        one step downward, the new node voilates the maxheap property then the method will recurse and 
        perform the same method again. This procedure takes O(logn base d where d is the the maximum number 
        children at node is d)time in worst case.
        """
        largest = node
        for k in range(1,self.maximumChildren+1):
            if self.child(k, node) <= self.heapSize and self.array[node] < self.array[self.child(k, node)]:
                if self.array[largest] < self.array[self.child(k, node)]:
                    largest = self.child(k, node)
        if largest != node:
            self.array[node], self.array[largest] = self.array[largest], self.array[node]
            self.maxHeapify(largest)

    def buildHeap(self):
        """
        Convert the array into d-ary maxheap. The loop starts from the last nonleaf node
        and starts running maxheapify procedure on the element. This procedure takes O(n) time.
        """
        self.heapSize = self.length - 1
        for nonLeaf in range(self.lastNonLeafNode, -1, -1):
            self.maxHeapify(nonLeaf)  

    def extractMax(self):
        """
        return and deletes the maximum priority element in the heap
        """
        maximum = self.array[0]
        self.array[0] = self.array[self.heapSize]
        self.heapSize -= 1
        self.maxHeapify(0)
        return maximum   

    def increaseKey(self,node: int, key: int)-> int:
        """
        Increases the element by the given value
        """
        if self.array[node] > key:
        	return 1
        else:
            self.array[node] = key
            while node > 0 and self.array[self.parent(node)] < key:
                self.array[self.parent(node)], self.array[node] = self.array[node], self.array[self.parent(node)]
                node = self.parent(node)

    def insert(self, key: int):
        """
        insert the new element into the heap
        """ 
        self.heapSize += 1
        self.array.append(float('-inf'))
        self.increaseKey(self.heapSize, key)  

    def delete(self, node: int):
        """
        this method deletes the element at nodeth location. It takes O(logn base d ) time
        """
        self.increaseKey(node, float('inf') )
        self.array[0], self.array[self.heapSize] = self.array[self.heapSize], self.array[0]
        self.heapSize -= 1
        self.maxHeapify(0)              	
    
    def __str__(self):
        tempList = []
        for i in range(0,self.heapSize + 1):
            tempList.append(self.array[i])
        tempList = [str(x) for x in tempList]
        return ' '.join(tempList)

def main():
    instance = DArrayHeap([8,14,32,6,1,9,17,4], 3)
    instance.buildHeap()
    print('The array after it has been coverted to dary max Heap is ',instance)
    maximum = instance.extractMax()
    print('The maximum element is ', maximum)
    print('The array after the maximum element has been removed is ', instance)
    flag = instance.increaseKey(5, 100)
    if flag == 1:
        print('The node value is greater than the value passed')
    else:    
        print('The array after the node has been changed to other value is ', instance)
    instance.insert(33) 
    print('The array after 33 is inserted in array is ', instance)  
    instance.delete(2)
    print('The array after deleting the node at 5 is', instance) 

if __name__ == '__main__':
    main()

