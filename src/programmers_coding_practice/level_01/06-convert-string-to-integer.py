"""
:reference: https://programmers.co.kr/learn/courses/30/lessons/12925?language=python3

:ASCII printable characters:
ord('+') = 43
ord('-') = 45
ord('0') = 48
ord('9') = 57
"""


def strToInt_01(s):
    return int(s)
    

def strToInt_02(s):
    
    rsl = 0
    for idx, each in enumerate(s[::-1]):
        if ord(each) <= 45: 
            rsl *= 1 if ord(each) - 45 else -1
        else:
            rsl += (ord(each) - 48) * pow(10, idx)
    
    return rsl
    


if __name__ == '__main__':
    N = '1234'
    # N = '-1234'
    # N = '+1234'
    
    print('solution_01:', strToInt_01(N))
    print('solution_02:', strToInt_02(N))