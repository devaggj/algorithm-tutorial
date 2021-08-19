def solution_01(n):
    
    return n if n < 10 else sum(map(int, str(n)))


def solution_02(n):
    
    if n < 10:
        return n
    
    return (n % 10) + solution_02(n // 10)
    
    


if __name__ == '__main__':
    N = 987
    
    print('solution_01:', solution_01(N))
    print('solution_02:', solution_02(N))