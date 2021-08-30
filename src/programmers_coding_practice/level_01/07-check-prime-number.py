"""
:reference: https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3
"""

def solution(n):
    
    count = 0
    for i in range(2, n + 1):
        if is_prime_number(i):
            count += 1
    
    return count

def is_prime_number(n):
    for i in range(2, int(pow(n, 1/2)) + 1):
        if n % i == 0:
            return False
        
    return True


def main():
    N = 10
    
    print(solution(N))

if __name__ == '__main__':
    main()