

class MaximumSubarray:
    def __init__(self, array):
        self.array = array 

    def maxSubarray(self):
        n = len(self.array)
        maximumProfit = -100000000000000
        for i in range(n):
            for j in range(i+1,n):
                profit = self.array[j] - self.array[i]
                if profit > maximumProfit:
                    maximumProfit = profit 
                    left = i 
                    right = j
        return left, right, maximumProfit
      
if __name__ == "__main__":
    instance = MaximumSubarray([10,11,7,10,6])
    left, right, profit = instance.maxSubarray()
    print('buy date=', left, 'sell date=', right, 'profit=', profit)                    