

import math
class MinMax:
    def __init__(self, sequence):
        self.sequence = sequence

    def minMaxDAC(self, i, j):
        if i == j:
            min, max = self.sequence[i], self.sequence[i]
            return min, max
        elif i == j-1:
            if self.sequence[i] < self.sequence[j]:
                min, max = self.sequence[i], self.sequence[j]
            else:
                min, max = self.sequence[j], self.sequence[i]
            return min, max
        else:
            mid =  math.floor((i + j)/2)
            min1, max1 = self.minMaxDAC(i, mid)
            min2, max2 = self.minMaxDAC(mid+1, j)
            if min1 < min2:
                min = min1
            else: min = min2
            if max1 > max2:
                max = max1
            else: max = max2
            return min, max

if __name__ == '__main__':
    instance = MinMax([1,6,23,66,0,45,64])
    min, max = instance.minMaxDAC(0,6)
    print(min, max)                       