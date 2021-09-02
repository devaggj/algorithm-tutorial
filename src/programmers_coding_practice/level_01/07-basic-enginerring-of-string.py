"""
:reference: https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3

[NOTE]
ord('0') == 48
ord('9') == 57
"""

def solution_x(s):
    if len(s) not in [4, 6]:
        return False
    
    for each in s:
        if ord(each) not in range(ord('0'), ord('9') + 1):
            return False
    return True

# regular expression
def solution_01(s):
    import re
    
    re_rsl = re.sub("[0-9]", '', s)
    if len(re_rsl) == 0 and len(s) in [4, 6]:
        return True
    
    return False

# try-except 
def solution_02(s):
    try:
        int(s)
    except:
        return False

    return len(s) in [4, 6]

# isdigit()
def solution_03(s):
    return s.isdigit() and len(s) in [4, 6]

def main():
    # S = "1234"
    S = "1234dasfesfd"
    
    print(solution_x(S))
    # print(solution_01(S))
    # print(solution_02(S))
    print(solution_03(S))

if __name__ == '__main__':
    main()
    