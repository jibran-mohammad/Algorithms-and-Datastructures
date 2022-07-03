"""
Program for sorting n numbers using selection sort.Time complexity of O(n^2) and space complexity if O(1)
"""


class SelectionSort:
    """
    class defining method sort and other operating overloading methods
    """
    def __init__(self,sequence):
        self.sequence= sequence   	
    
    def sort(self):
        for i in range(0,len(self.sequence)-1):
        	min= i
        	for j in range(i+1,len(self.sequence)):
        	    if self.sequence[j] < self.sequence[min]:
        	        min= j
        	self.sequence[i],self.sequence[min]= self.sequence[min],self.sequence[i]
    
    def __repr__(self):
        return 'The sorted sequence is %s ' % self.sequence


if __name__ == '__main__':
    instance =SelectionSort([4,5,2,1,0,34,67,4,34,2,66])
    instance.sort()
    print(instance)
        