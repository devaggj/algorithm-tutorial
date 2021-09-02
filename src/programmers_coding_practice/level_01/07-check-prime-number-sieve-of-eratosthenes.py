"""
:reference: https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3

ref_wiki: https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
"""

def solution_01(n):
    sieve = [True] * n    
    
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False
    
    prime_list = []
    for i in range(2, n):
        if sieve[i] == True:
            prime_list.append(i)
    
    return len(prime_list)
    # return [ i for i in range(2, n) if sieve[i] == True ]

def solution_02(n):
    num = set(range(2, n + 1))
    
    for i in range(2, int(n ** 0.5) + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    
    return len(num)


def main():
    N = 10
    
    print(solution_01(N))
    print(solution_02(N))

if __name__ == '__main__':
    main()