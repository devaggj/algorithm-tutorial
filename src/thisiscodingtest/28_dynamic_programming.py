"""
[LINK] https://www.youtube.com/watch?v=rWbjQphRE9A&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=28&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF]
[TITLE] 28강 다이나믹 프로그래밍 개요
"""

d = [0] * 100

## top -> down
def fibo_top_down(n):
    print(f'f({n})', end=' ')

    # 종료 조건 (1 혹은 2일 경우 1을 반환)
    if n == 1 or n == 2:
        return 1

    # 이미 계산한 적 있는 문제리면 그대로 반환
    if d[n] != 0:
        return d[n]

    # 아직 계산하지 않은 문제라면 '점화식'에 따라서 피보나치 결과 반환
    d[n] = fibo_top_down(n-1) + fibo_top_down(n-2)

    return d[n]

## bottom -> up
def fibo_bottom_up(n):
    for i in range(1, n + 1):
        if i < 3:
            d[i] = 1
            continue
        d[i] = d[i - 1] + d[i - 2]

    return d[n]


def main():
    n1 = 6
    n2 = 99

    import time
    start_time = time.time()
    print(fibo_top_down(n1))
    print(fibo_bottom_up(n2))

    end_time = time.time()
    print("time:", end_time - start_time)

###
main()
