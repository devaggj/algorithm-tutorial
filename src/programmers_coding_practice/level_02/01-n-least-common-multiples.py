"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3
:ref:
"""

from functools import reduce

def solution(arr):

    input = arr
    for i in range(len(arr) - 1):
        for j, val in enumerate(arr[i+1:]):
            if val % arr[i] == 0:
                input[j+1] = int(val / arr[i])

    return reduce(lambda x, y: x * y, input)


def main():
    arr = [2,6,8,14]
    print(solution(arr))

if __name__ == "__main__":
    main()
