

class InsertionSort:
    def __init__(self, sequence):
        self.sequence = sequence

    def sort(self, n):
        if n <= 2:
            return
        else:
            self.sort(n-1)
            self.insert(n-2, n-1)

    def insert(self, i, j):
        key = self.sequence[j]
        while i >=0 and key < self.sequence[i]:
            self.sequence[i+1] = self.sequence[i]
            i -= 1
        self.sequence[i+1] = key
   
    def __str__(self):
        return 'Sorted sequence is %s' % self.sequence

if __name__ == '__main__':
    instance = InsertionSort([34,23,11,44,7,0,24])
    instance.sort(len(instance.sequence))
    print(instance)