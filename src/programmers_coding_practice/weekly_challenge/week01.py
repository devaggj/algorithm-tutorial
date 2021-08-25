"""
https://programmers.co.kr/learn/courses/30/lessons/82612?language=python3
"""

def solution(price, money, count):
    total = price * count * (count + 1) / 2 
    return total - money if total > money else 0


if __name__ == '__main__':
    
    p = 3
    m = 20
    c = 4
    
    print(solution(p, m, c))
    