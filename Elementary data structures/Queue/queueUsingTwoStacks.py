"""
Implemention of Queue using two Stacks. The enqueue operation takes O(1) time in worst case. The dequeue opeartion
takes O(n) time in worst case and using amortized analysis, on average it takes O(1) time.
"""

class Queue:
    """
    class Queue defining two dundar methods and two other methods name enqueue and dequeue.
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.top1 = -1
        self.top2 = -1

    def enqueue(self, element: int)-> None:
        """
        This method will always take O(1) time. It will always push the element on stack 1. Stack1 is assumed
        to be of unlimited size.
        """
        self.stack1.append(element)
        self.top1 +=1

    def dequeue(self)-> int:
        """
        This method on average will take O(1) time for dequeing. In worst case, it will have some operations 
        that will take O(n) time assuming n to be the length of stack1. The worst case will occurr if the 
        stack2 is empty, then we will pop every element from stack1 and push it to stack2, if i assume the number
        of elements in stack1 are n, then time complexity of that dequeue operation will be O(n).
        """
        if not self.stack2 and not self.stack1:
            print('Underflow')
        else:
            if not self.stack2:
                for index in range(self.top1 + 1):
                    self.stack2.append(self.stack1.pop())
                    self.top2 += 1
                    self.top1 -= 1
                self.top2 -= 1    
                return self.stack2.pop()
            else:
                self.top2 -= 1
                return self.stack2.pop()
    
    def __repr__(self):
        if not self.stack1 and not self.stack2:
    	    tempList = []
        elif not self.stack1 and self.stack2:
    	    tempList = [self.stack2[index] for index in range(self.top, -1, -1)]
        elif self.stack1 and self.stack2:
            tempList = [self.stack2[index] for index in range(self.top2, -1, -1)]
            tempList2 = [self.stack1[index] for index in range(self.top1 + 1)]
            tempList = tempList + tempList2
        else:        
            tempList = [self.stack1[index] for index in range(self.top1 + 1)]
        return f'The element in the queue are {tempList}'

def main():
    instance = Queue()
    instance.dequeue()
    instance.enqueue(5)
    instance.enqueue(4)
    instance.enqueue(78) 
    print(instance)
    element = instance.dequeue()
    print(f'The dequeued element is {element}')
    instance.enqueue(44)
    print(instance)

if __name__ == '__main__':
    main()           