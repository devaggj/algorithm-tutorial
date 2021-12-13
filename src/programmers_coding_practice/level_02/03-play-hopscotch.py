"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3
:ref: https://eda-ai-lab.tistory.com/480
"""

import time

def solution(land):
    for i in range(1, len(land)):
        # self = 0
        for j in range(len(land[0])):
            last = land[i-1][:]
            last[j] = 0
            land[i][j] = max(last) + land[i][j]
            # self += 1

    return max(land[-1])


def main():
    land = [
            [1,2,3,5],
            [5,6,7,8],
            [4,3,2,1]
        ]
    start_time = time.time()
    print(solution(land))

    end_time = time.time()
    print("time:", end_time - start_time)

if __name__ == "__main__":
    main()
