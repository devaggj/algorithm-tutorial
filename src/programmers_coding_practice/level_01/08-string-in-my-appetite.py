"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
"""

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))



if __name__ == '__main__':
    S = ["sun", "bed", "car"]
    n = 1
    
    print(solution(S, n))
    