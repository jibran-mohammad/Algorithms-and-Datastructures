
import math
class BinarySearch:
    def __init__(self, sequence,):
        self.sequence = sequence
        self.index = 0

    def bs(self,i,j,x):
        if i == j:
           if self.sequence[i] == x:
           	    self.index = i
           else:
           	    self.index = None
        else:
            mid = math.floor((i + j)/2)
            if self.sequence[mid] == x:
                self.index = mid
            else:
                if x < self.sequence[mid]:
                    self.bs(i, mid, x)
                else:
                    self.bs(mid+1, j, x)

if __name__ == "__main__":
    instance = BinarySearch([0,3,5,23,45,65,77])
    instance.bs(0,6,65)
    print(instance.index)
