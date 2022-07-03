"""
Program for sum of two n bit numbers stored in the list of size n+1. Time complexity of O(n) and space 
is O(n) because we are storing the resulting sum into the array of size n+1
"""

class Sum:
    """
    Class for defining the data and methods for sum of two n bit numbers
    """
    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2
        self.resultlist = [None for x in range(0,len(list1) + 1)]

    def sumOfTwoNBitNumbers(self):
        carry= 0

        for i in range(len(self.list1)-1,-1,-1):
            self.resultlist[i+1]= (self.list1[i] + self.list2[i] + carry) % 2
            if (self.list1[i] + self.list2[i] + carry) >= 2:
        	    carry= 1
            else:
                carry= 0
        self.resultlist[0]= carry
    
    def __repr__(self):
        return 'The sum of two n bit numbers is %s ' % self.resultlist

def main():
    instance= Sum([1,0,1,1,0],[1,1,0,1,1])
    instance.sumOfTwoNBitNumbers()
    print(instance) 

if __name__ == '__main__':
    main()           	