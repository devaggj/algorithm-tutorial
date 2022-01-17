"""
:link: https://programmers.co.kr/learn/courses/30/lessons/87390?language=python3
:ref:
"""

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        x = i // n
        y = i % n
        num = max(x, y) + 1
        answer.append(num)

    return answer

def solution2(n, left, right):
    answer = []
    while left <= right:
        answer.append(max(left // n, left % n) + 1)
        left += 1

    return answer

def main():

    # return [3,2,2,3]
    n = 3
    left = 2
    right = 5

    import time
    start_time = time.time()
    print(solution2(n, left, right))

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
