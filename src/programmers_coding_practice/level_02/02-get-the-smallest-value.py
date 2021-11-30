"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12941?language=python3
:ref:
"""

def solution(A, B):

    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer


def solution2(A, B):
    return sum(map(lambda a, b: a * b, sorted(A), sorted(B, reverse=True)))


def main():
    A = [1, 2]
    B = [3, 4]
    print(solution(A, B))
    print(solution2(A, B))


if __name__ == "__main__":
    main()
