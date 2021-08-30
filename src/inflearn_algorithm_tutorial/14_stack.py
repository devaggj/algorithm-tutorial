"""
:reference: https://binaryjourney.tistory.com/123

library를 사용치않고 Stack을 직접 구현
"""

class Stack:
    
    def __init__(self):
        self.top = []
    
    def length(self):
        return len(self.top)
    
    def empty(self) -> bool:
        return len(self.top) == 0
    
    def push(self, item):
        self.top.append(item)
    
    def pop(self):
        if not self.empty():
            return self.top.pop(-1)
        else:
            print("IndexError: list index out of range")
            exit()
    
    def peek(self):
        if not self.empty():
            return self.top[-1]
        else:
            print("IndexError: list index out of range")
            exit()
    
    def print(self):
        print(self.top)


def main():
    stack = Stack()
    
    stack.push(4)
    stack.push(7)
    stack.push(0)
    stack.push(9)
    stack.print()
    
    print(stack.peek())
    stack.print()
    
    print(stack.pop())
    stack.print()
    

if __name__ == '__main__':
    main()
    
    