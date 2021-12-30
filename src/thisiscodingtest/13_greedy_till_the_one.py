"""
:link: https://www.youtube.com/watch?v=_TG0hVYJ6D8&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=13&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
:ref:
"""

def solution(n, k):
    result = 0

    while True:
        # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
        target = (n // k) * k
        result += n - target
        n = target

        # n이 k보다 작을 때 (더 이상 나눌 수 없을 때 반복문 break)
        if n < k:
            break

        # k로 나누기
        result += 1
        n //= k

    print(n)
    result += (n - 1)
    return result


def main():
    n = 25
    k = 3

    import time
    start_time = time.time()
    print(solution(n, k))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
