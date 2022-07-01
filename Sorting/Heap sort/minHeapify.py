

class MinHeapify:
    def __init__(self, sequence):
        self.sequence = sequence

    def minheapify(self, i):
        l = (2 * i) + 1
        r = (2 * i) + 2

        if l <= len(self.sequence) and self.sequence[l] < self.sequence[i]:
            smallest = l 
        else:
            smallest = i 

        if r <= len(self.sequence) and self.sequence[r] < self.sequence[smallest]:
            smallest = r 

        if smallest != i:
            self.sequence[i], self.sequence[smallest] = self.sequence[smallest], self.sequence[i]
            self.minheapify(smallest)

if __name__ == '__main__':
    instance = MinHeapify([16,7,13,4,3,27,17])
    instance.minheapify(0)
    print(instance.sequence)                
          
                   
