"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3
:ref:
"""

import time

def solution(n):
    count_one = bin(n)[1:].count('1')
    next = n + 1
    while True:
        if count_one == bin(next)[1:].count('1'):
            break
        next += 1

    return next


def main():
    n = 78  # should return 83
    start_time = time.time()
    print(solution(n))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
