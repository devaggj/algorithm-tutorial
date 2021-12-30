"""
:link: https://www.youtube.com/watch?v=5OYlS2QQMPA&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=13&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
:ref:
"""

def solution(price, coins):
    n = price
    count = 0

    for coin in coins:
        count += n // coin  # 나머지를 제외한 몫만 할당
        n %= coin           # 몫이 아닌 나머지만 할당

    return count


def main():
    price = 1260
    coins = [ 500, 100, 50, 10 ]

    import time
    start_time = time.time()
    print(solution(price, coins))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
