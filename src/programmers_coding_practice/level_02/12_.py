"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/86052?language=python3
[REF] https://velog.io/@mein-figur/ProgrammersPython%EB%B9%9B%EC%9D%98-%EA%B2%BD%EB%A1%9C-%EC%82%AC%EC%9D%B4%ED%81%B4
[TITLE] 빛의 경로 사이클
"""

import sys
sys.setrecursionlimit(10 ** 6)

def solution(grid):

    d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    right = {0: 3, 1: 2, 2: 0, 3: 1}
    left = {0: 2, 1:3, 2: 1, 3: 0}

    answer = []
    w, h = len(grid[0]), len(grid)
    cases = [[[1]*4 for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            for i in range(4):
                if not cases[y][x][i]:
                    continue

                cnt = 0
                ty, tx, ti = y, x, i
                while True:
                    cases[ty][tx][ti] -= 1
                    cnt += 1
                    now = grid[ty][tx]

                    if now == 'L':
                        ti = left[ti]
                    elif now == 'R' :
                        ti = right[ti]
                    tx, ty = (tx+d[ti][1])%w, (ty+d[ti][0])%h
                    if tx == x and ty == y and ti == i:
                        break
                answer.append(cnt)

    answer.sort()
    return answer

def main():
    grid = ["SL","LR"]

    import time
    start_time = time.time()
    print(solution(grid))

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
