"""
refernce: https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3
"""

def solution_01(s):
    
    strange_txt = ''
    for i in s.split(' '):
        for j, each in enumerate(i):
            if j % 2 == 0:
                strange_txt += each.upper()
            else:
                strange_txt += each.lower()
                
        strange_txt += ' '
        
    return strange_txt[:-1]
    # return strange_txt.rstrip()   # 문제에서는 통과 못했던 방법


def solution_02(s):
    
    return ' '.join(map(lambda s: ''.join([each.upper() if idx % 2 == 0 else each.lower() for idx, each in enumerate(s)]), s.split(' ')))



if __name__ == '__main__':
    s = "try hello world"
    
    print('solution_01:', solution_01(s))
    print('solution_02:', solution_02(s))