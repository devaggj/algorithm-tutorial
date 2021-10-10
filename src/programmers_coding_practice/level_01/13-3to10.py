"""
:link: https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3
:ref: https://hmkim312.github.io/posts/3%EC%A7%84%EB%B2%95_%EB%92%A4%EC%A7%91%EA%B8%B0/
"""

def solution(n):
    answer = ''
    while n > 0:
        quotient, remainder = divmod(n, 3)
        answer += str(remainder)
        n = quotient
    return int(answer, base = 3)


def main():
    n = 45
    print(solution(n))
    
if __name__ == "__main__":
    main()
