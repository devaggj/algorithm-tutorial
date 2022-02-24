"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/12980?language=python3
[REF]
[TITLE] 점프와 순간 이동
"""

def solution(n):
    result = 0

    while n > 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            result += 1

    return result


def main():
    n = 5000    # return 5

    import time
    start_time = time.time()
    print(solution(n))

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
