"""
reference: https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3
"""

def solution_01(n):
    
    # .reverse() 사용할 경우 return 값 없음
    # reversed(n) 사용할 경우 return 값이 있어 map 안에 사용 가능
    
    return list(map(int, reversed(str(n))))
    

def solution_02(n):
    
    return list(map(int, list(str(n))[::-1]))
    
    
    
if __name__ == "__main__":
    N = 12345
    
    print('solution_01:', solution_01(N))
    print('solution_02:', solution_02(N))