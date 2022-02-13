"""
[LINK] https://www.youtube.com/watch?v=e7_H8SLZlHY&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=20
[REF]
[TITLE] [이것이 코딩 테스트다 with Python] 20강 DFS & BFS 기초 문제 풀이
"""

n = 4
m = 5
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


def solution():
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)


def main():
    import time
    start_time = time.time()
    solution()

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
