

class Stack:
    def __init__(self, array):
        self.array= array
        self.top = -1

    def stackEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, x):
        self.top += 1
        self.array.append(x)
        self.array[self.top] = x

    def pop(self):
        if self.stackEmpty():
            print('Stack is empty')
        else:
            self.top -= 1
            return self.array[self.top + 1]
    
    def __str__(self):
        tempList = []
        j = 0
        for i in self.array:
            if j <= self.top:
                tempList.append(i)
                j += 1
        return 'The stack is: %s' % tempList
                
if __name__ == '__main__':
    instance = Stack([])
    instance.push(7)
    instance.push(1)
    print(instance)
    print(instance.pop())
    print(instance)                                    