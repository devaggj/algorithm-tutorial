"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3
:ref:
"""

def solution(s):
    intArr = list(map(int, s.split(" ")))
    return str(min(intArr)) + " " + str(max(intArr))



def main():
    # s = "1 2 3 4"
    s = "-1 -2 -3 -4"
    print(solution(s))

if __name__ == "__main__":
    main()
