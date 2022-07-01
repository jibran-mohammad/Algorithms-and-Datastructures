"""
Code for sorting n elements using merge sort
"""

import math
import sys


class MergeSort:
    """
    MergeSort class containing __init__ for defining the instance attributes likes sequence which has
    to be sorted and p,q to be the first and last indices. It's a divide and conquer algorithm which
    contains mergeProcedure method for combine step and mergeSort procedure for divide step
    """
    def __init__(self,sequence:list):
        self.sequence= sequence
        self.p= 0
        self.r= len(sequence) - 1
    
    def mergeProcedure(self,p: int, q: int, r: int):
        """
        Combining the solution of two subproblems to get the solution of original subproblem
        subarrays will be sequence[p-q] and sequence[q+1 - r].The procedure assumes that both subarray are 
        sorted
        """

        # calculating the length of ist subarray
        n1= q - p + 1

        # calculating the length of second subarray
        n2= r - q

        # creating two additional subarrays and assigning them the subarrays of original sequence
        l1= [self.sequence[p + i] for i in range(n1)]
        l2= [self.sequence[q + i + 1] for i in range(n2)]

        # assigning infinity to the end of subarrays created 
        l1.append(float('inf'))
        l2.append(float('inf'))

        # calculating the length of the array and assigning indices i and j to two subarrays
        n= r - p + 1
        i=0
        j=0; k=p
        for _ in range(n):
            if l1[i] <= l2[j]:
                self.sequence[k]= l1[i]
                k += 1
                i += 1
            else:
                self.sequence[k]= l2[j]
                j += 1
                k += 1  

    def mergeSort(self, p: int ,r: int):
        """
        Divide and conquer step of divide and conquer strategy
        """

        if p < r:

            # Dividing the array into two subarrays
            q= math.floor((p+r)/2)

            # solving the two subarrays recursively
            self.mergeSort(p, q)
            self.mergeSort(q+1, r)

            # calling the combine procedure
            self.mergeProcedure(p, q, r)

    def __str__(self):
        return 'Sorted Sequence is %s' % self.sequence        


def main():
    instance = MergeSort([5,6,22,98,23,0,12])
    instance.mergeSort(instance.p,instance.r)
    print(instance)

if __name__=="__main__":
    main()