"""
:link: https://www.youtube.com/watch?v=gFpKGWdEE5g&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=17
:ref:
"""

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    sss = 5

    import time
    start_time = time.time()
    # return 120
    print(factorial_iterative(sss))
    print(factorial_recursive(sss))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
