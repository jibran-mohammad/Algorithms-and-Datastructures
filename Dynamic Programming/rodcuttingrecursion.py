"""
Implementation of RodCutting Problem where the length of rod is assumed to be n. I have given an array which 
contains the price associated with each rod length. Now my job is to cut the rod in a way so as to maximize the
total revenue. The solution used here to implement the Rodcutting problem is recursive top- down solution. If
I cut the rod at first position, assuming the rod length to be 10, now i would be left with rod of length one
and rod of length 9, these are the same problems in nature but of smaller size. I can cut the rod at 1,2,3,4,
.... 10. Cutting the rod at 10 means I don't need to cut it, without cutting it, I am getting the maximum revenue
now i have to consider all the possible cases and select the maximum out of them. With the help of recursion
I can solve the subproblems of same nature with smaller size. If you draw of tree out of this recursion, the
height of the tree will be proportional to the length of the rod, and assuming the tree would be complete, the 
number of nodes in the tree would be more than  O(2 ^ n). Assuming it takes constant time to solve every subprolem
which is some cases, it doesn't. The time complexity of this algorithm would be O(2^n) and space complexity
would be O(n)(height of the tree)
"""

class RodCutting:
    """
    class RodCutting defining one dundar method for initialization and one recursive method name rodCutting.
    """
    def __init__(self, priceArray: list):
        self.priceArray = priceArray

    def rodCutting(self,n):
        if n == 0:
           return 0
        q = float('-inf')
        for i in range(n):
            q= max(q, self.priceArray[i] + self.rodCutting(n - (i + 1)))   
        return q

def main():
    instance = RodCutting([1,5,8,9,10,17,17,20,24,30])
    revenue = instance.rodCutting(8)
    print(f"The revenue obtained by cutting the rod of length 8 is {revenue}")
    revenue = instance.rodCutting(10)
    print(f"The revenue obtained by cutting the rod of length 10 is {revenue}")

if __name__ == '__main__':
    main()    
