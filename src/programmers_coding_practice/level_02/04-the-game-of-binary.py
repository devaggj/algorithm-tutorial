"""
:link: https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3
:ref: https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-n%EC%A7%84%EC%88%98-%EA%B2%8C%EC%9E%84-Python
:ref: https://velog.io/@dogcu/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-n%EC%A7%84%EC%88%98-%EA%B2%8C%EC%9E%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""

def convert(num, base):
    tmpr = '0123456789ABCDEF'
    quotient, remainder = divmod(num, base)

    if quotient == 0:
        return tmpr[remainder]
    else:
        return convert(quotient, base) + tmpr[remainder]

def solution(n, t, m, p):
    game = ''
    for i in range(t * m):
        game += str(convert(i, n))

    result = ''
    while len(result) < t:
        result += game[p - 1]
        p += m

    return result


def main():
    '''
    진법 n,
    미리 구할 숫자의 갯수 t,
    게임에 참가하는 인원 m,
    튜브의 순서 p
    '''

    import time

    n, t, m, p = 2, 4, 2, 1     # should return "0111"
    # n, t, m, p = 16, 16, 2, 1   # should return "02468ACE11111111"

    start_time = time.time()
    print(solution(n, t, m, p))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
