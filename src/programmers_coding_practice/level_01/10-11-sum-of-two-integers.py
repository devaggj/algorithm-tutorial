"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3
"""

def solution(a, b):
    if a == b: return a
    start, end = min(a, b), max(a, b)
    return sum(i for i in range(start, end + 1))

def solution2(a, b):
    return (abs(a-b) + 1) * (a+b) // 2

def main():
    int1 = 5;
    int2 = 3; 
    print(solution2(int1, int2))
    
if __name__ == "__main__":
    main()