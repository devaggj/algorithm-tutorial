"""
https://www.acmicpc.net/problem/10989
"""

def solution(list, n):
    
    serial = [0] * n
    
    for each in list:
        serial[each - 1] += 1
    
    for i in range(0, n):
        while serial[i] != 0:
            print(i + 1)
            serial[i] -= 1
            
            
            
if __name__ == "__main__":
    N = 10
    example = [5, 2, 3, 1, 4, 2, 3, 5, 1, 7]
    print(solution(example, N))
