"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12945?language=python3
:ref:
"""

def solution(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b % 1234567

    #  if n <= 2: return 1
    # return (solution(n-2) + solution(n-1)) % 1234567

def main():
    n = 5
    print(solution(n))

if __name__ == "__main__":
    main()
