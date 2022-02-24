"""
[LINK] https://velog.io/@study-dev347/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B9%9B%EC%9D%98-%EA%B2%BD%EB%A1%9C-%EC%82%AC%EC%9D%B4%ED%81%B4
[REF] https://nbalance97.tistory.com/196
[TITLE]
"""

import sys
sys.setrecursionlimit(10 ** 6)

direction = [ [0, -1], [1, 0], [0, 1], [-1, 0] ]

def bfs(grid, visited, vector):
    row, col = len(grid), len(grid[0])
    y, x, i = vector
    count = 0

    while True:
        if visited[y][x][i]:
            break

        visited[y][x][i] = 1
        count += 1

        if grid[y][x] == "S":
            pass
        elif grid[y][x] == "L":
            i = (i + 1) % 4
        elif grid[y][x] == "R":
            i = (i - 1) % 4

        y = (y + direction[i][0]) % row
        x = (x + direction[i][1]) % col

    return count


def solution(grid):
    row, col = len(grid), len(grid[0])
    answer = []
    visited = [ [ [0] * 4 for _ in range(col) ] for _ in range(row) ]
    for y in range(row):
        for x in range(col):
            for i in range(4):
                if visited[y][x][i]:
                    continue
                answer.append(bfs(grid, visited, [y, x, i]))

    return sorted(answer)


def main():
    grid = ["SL", "LR"]

    import time
    start_time = time.time()
    print(solution(grid))

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
