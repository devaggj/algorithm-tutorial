"""
:link: https://programmers.co.kr/learn/courses/30/lessons/86491?language=python3
"""

def solution(sizes):
    w = 1
    h = 1
    for i in sizes:
        mx = max(i[0], i[1])
        mn = min(i[0], i[1])
        if mx > w: w = mx
        if mn > h: h = mn  
    return w * h


def main():
    s = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(s))
    
if __name__ == "__main__":
    main()