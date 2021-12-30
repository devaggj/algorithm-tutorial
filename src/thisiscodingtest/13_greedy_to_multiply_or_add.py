"""
:link: https://www.youtube.com/watch?v=_TG0hVYJ6D8&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=13&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
:ref:
"""

def solution(num_string):

    result = int(num_string[0])

    for i in num_string[1:]:
        num = int(i)
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num

    return result


def main():
    sss = "02984"

    import time
    start_time = time.time()
    print(solution(sss))    # return 576

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
