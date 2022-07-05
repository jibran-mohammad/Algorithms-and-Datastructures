"""
Algorithm for multiplication of two square matrices. Iterative solution. The algorithm  has O(n^3) as 
time complexity and O(n^2) as space complexity
"""

class MatrixMultiplication:
    def __init__(self, matrix1: list, matrix2: list):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.row = len(self.matrix1)
        self.result = [ [0 for i in range(len(matrix1))] for j in range(len(matrix2))]

    def multiplication(self):
        for i in range(self.row):
            for j in range(self.row):
                element = 0
                for k in range(self.row):
                    element = element + self.matrix1[i][k] * self.matrix2[k][j] 
                self.result[i][j] = element

    def __repr__(self):
        return 'The multiplication of two matrices is %s' % self.result

def main():
    instance = MatrixMultiplication([[1,4,5], [5,6,7,],[8,5,4]], [[1,2,3], [6,5,9],[0,1,2]])
    instance.multiplication()
    print(instance)

if __name__ == '__main__':
    main()                        
                       