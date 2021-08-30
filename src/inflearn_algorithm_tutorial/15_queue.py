"""
:reference: https://binaryjourney.tistory.com/124

library를 사용치않고 Queue를 직접 구현
library를 사용하여 dequeue 적용
"""

class Queue:
    
    def __init__(self):
        self.queue = []
    
    def length(self):
        return len(self.queue)
    
    def empty(self) -> bool:
        return len(self.queue) == 0

    def push(self, item):
        self.queue.append(item)
        # self.queue.insert(0, item)    # same result
    
    def pop(self):
        if not self.empty():
            return self.queue.pop(0)
        else:
            print("IndexError: list index out of range")
            exit()
    
    def peek(self):
        if not self.empty():
            return self.queue[0]
        else:
            print("IndexError: list index out of range")
            exit()
    
    def print(self):
        print(self.queue)


def main():
    queue = Queue()

    queue.push(4)
    queue.push(7)
    queue.push(0)
    queue.push(9)
    queue.print()
    
    print(queue.peek())
    queue.print()
    
    print(queue.pop())
    queue.print()

if __name__ == '__main__':
    main()