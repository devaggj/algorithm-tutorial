"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3
"""

def solution_x(s):
    ascii_p, count_p = [80, 112], 0
    ascii_y, count_y = [89, 121], 0
    for each in s:
        if ord(each) in ascii_p:
            count_p += 1
        elif ord(each) in ascii_y:
            count_y += 1

    return count_p == count_y

def solution_01(s):
    return s.lower().count('p') == s.lower().count('y')

def main():
    S = "pPoooyY"
    
    print(solution_x(S))
    print(solution_01(S))

if __name__ == '__main__':
    main()