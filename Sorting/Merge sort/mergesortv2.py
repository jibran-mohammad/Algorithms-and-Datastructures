
import math

class MergeSort:
    def __init__(self,sequence):
        self.sequence= sequence
        self.p= 0
        self.r= len(sequence) - 1
    
    def mergeProcedure(self,p,q,r):
        n1= q - p + 1
        n2= r - q
        l1= [self.sequence[p + i] for i in range(n1)]
        l2= [self.sequence[q + i + 1] for i in range(n2)]
        i=0
        j=0; k=p
        while i < n1 and j < n2:
            if l1[i] <= l2[j]:
                self.sequence[k]= l1[i]
                i += 1
                k += 1
            else:
                self.sequence[k]= l2[j]
                j += 1
                k += 1
        if i >= n1 and j < n2:
            while j < n2:
                self.sequence[k] = l2[j]
                j +=1
                k +=1
        elif j >= n2 and i < n1:
            while i < n1:
                self.sequence[k] = l1[i]
                i += 1
                k += 1 
        
    def mergeSort(self,p,r):
        if p < r:
            q= math.floor((p+r)/2)
            self.mergeSort(p, q)
            self.mergeSort(q+1, r)
            self.mergeProcedure(p, q, r)
    
    def __str__(self):
        return 'Sorted sequence is %s' % self.sequence
if __name__=="__main__":
    instance = MergeSort([4,6,8,22,0,65,45])
    instance.mergeSort(instance.p,instance.r)
    print(instance)
    