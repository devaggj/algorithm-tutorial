"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12924?language=python3
:ref:
"""

def solution(n):
    count = 0
    for i in range(1, n):
        if i > n // 2:
            break

        num = 0
        for j in range(i, n):
            num += j
            if num == n:
                count += 1
                break
            elif num > n:
                break

    return count + 1


def main():
    n = 15
    print(solution(n))


if __name__ == "__main__":
    main()
