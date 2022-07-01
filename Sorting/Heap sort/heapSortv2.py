

class HeapSort:
    def __init__(self, sequence):
        self.sequence = sequence

    def maxHeapify(self, i):
        while i < len(self.sequence):
            l = (2 * i) + 1
            r = (2 * i) + 2
            
            if l <= len(self.sequence) and self.sequence[l] > self.sequence[i]:
                largest = l 
            else:
                largest = i 
            
            if r <= len(self.sequence) and self.sequence[r] > self.sequence[largest]:
                largest = r 

            if largest != i:
                self.sequence[i], self.sequence[largest] = self.sequence[largest], self.sequence[i]
                i = largest
            else:
                break

if __name__ == '__main__':
    instance = HeapSort([27,17,3,16,13,10,1,5,7,12,4,8,9,0])
    instance.maxHeapify(2)
    print(instance.sequence)                    