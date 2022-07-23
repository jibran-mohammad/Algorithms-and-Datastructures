"""
Implementing two stacks using single array such that the push and pop operation will take O(1) time for both
stacks and no memory should be wasted. We start the stack1 from initial position of the array and stack2 from
final position of the array, thus the stacks will grow in opposite sides which will make sure that no memory 
locatin of an array is wasted
"""

class TwoStacks:
    """
    class TwoStacks has two dundar methods and four other methods named pushStackOne, pushStackTwo, popStackOne,
    popStackTwo
    """
    def __init__(self, size: int):
        self.array = [None for i in range(size)]
        self.length = size
        self.top1= -1
        self.top2= size

    def pushStackOne(self, element: int):
        """
        This method will push the element in the stack one. The overflow condition is if top attribute of stack
        one is one step behind the top attribute of stack two.
        """
        if self.top1 + 1 == self.top2:
            print('Overflow')
        else:
            self.top1 += 1
            self.array[self.top1] = element

    def pushStackTwo(self, element: int):
        """
        This method will push the element in the stack two. The overflow condition is if top attribute of stack
        one is one step behind the top attribute of stack two.
        """
        if self.top2 - 1 == self.top1:
            print('Overflow')
        else:
            self.top2 -= 1
            self.array[self.top2] = element

    def popStackOne(self)-> int:
        """
        This method will pop element from stack one
        """
        if self.top1 == -1:
            print('Underflow')
        else:
            self.top1 -= 1
            return self.array[self.top1 + 1]

    def popStackTwo(self)-> int:
        """
        This method will pop element from stack two
        """
        if self.top2 == self.length:
            print('Underflow')
        else:
            self.top2 += 1
            return self.array[self.top2 + 1] 

    def __repr__(self):
        stack1 = [self.array[index] for index in range(self.top1 + 1)]
        stack2 = [self.array[index] for index in range(self.length - 1, self.top2 - 1, -1)]
        return f"The elemnts in stack1 are {stack1} and the elements in stack2 are {stack2}, top1= {self.top1}, top2 = {self.top2}"

def main():
    instance = TwoStacks(10) 
    instance.popStackOne()
    instance.popStackTwo()
    instance.pushStackOne(1)
    instance.pushStackOne(5)
    instance.pushStackOne(7)
    instance.pushStackOne(8)
    instance.pushStackOne(32)
    instance.pushStackTwo(5)
    instance.pushStackTwo(84)
    instance.pushStackTwo(62)
    instance.pushStackTwo(91)
    instance.pushStackTwo(48)
    print(instance)
    instance.pushStackTwo(545)
    print(instance)
    instance.popStackOne()
    print(instance)
    instance.popStackTwo()
    print(instance)

if __name__ == '__main__':
    main()