from collections import deque

def main():
    
    que = deque()
    
    que.append(1)
    que.append(2)
    que.append(3)
    que.append(4)
    print(que)
    
    que.popleft()
    print(que)
    
    que.appendleft(9)
    print(que)
    
if __name__ == '__main__':
    main()