"""
:link: https://www.youtube.com/watch?v=QhMY4t2xwG0&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=15&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
:ref:
"""

'''완전탐색 유형'''
def solution(h):
    count = 0
    for hr in range(h + 1):
        for mm in range(60):
            for ss in range(60):
                clock = "" + str(hr) + str(mm) + str(ss)
                if clock.find('3') > -1:
                    count += 1

    return count


def main():
    h = 5

    import time
    start_time = time.time()
    print(solution(h))  # return 11475

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
