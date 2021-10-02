"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3
"""

def solution(s):
    ln = len(s)
    return s[ln // 2] if ln % 2 else s[ln // 2 - 1 : ln // 2 + 1]
    
def solution2(s):
    a = len(s)
    if a % 2 == 0:
        a = (a-2) / 2
    else:
        a = (a-1) / 2
    return s[int(a) : -int(a)]
    
def main():
    # string = "abcde"    # "c"
    string = "qwer"     # "we"
    print(solution2(string))
    
if __name__ == "__main__":
    main()
