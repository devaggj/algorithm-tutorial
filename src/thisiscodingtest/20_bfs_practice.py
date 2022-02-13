"""
[LINK] https://www.youtube.com/watch?v=e7_H8SLZlHY&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=20
[REF]
[TITLE] [이것이 코딩 테스트다 with Python] 20강 DFS & BFS 기초 문제 풀이
"""

from collections import deque

n = 5
m = 6
graph = [[1, 0, 1, 0, 1, 0],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    deq = deque()
    deq.append((x, y))

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                deq.append((nx, ny))

    return graph[n-1][m-1]


def solution():
    print(bfs(0, 0))


def main():

    import time
    start_time = time.time()
    solution()

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
