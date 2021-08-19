def solution_01(n):
    answer = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    
    return answer


def solution_02(n):
    
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])


if __name__ == '__main__':
    N = 12
    
    print('solution_01:', solution_01(N))
    print('solution_02:', solution_02(N))