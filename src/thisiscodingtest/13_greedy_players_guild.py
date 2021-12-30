"""
:link: https://www.youtube.com/watch?v=_TG0hVYJ6D8&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=13&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
:ref:
"""

def solution(players, performance):

    performance.sort()

    result = 0
    count = 0

    for stat in performance: 
        count += 1
        if count >= stat:
            result += 1
            count = 0

    return result


def main():
    players = 5
    performance = [ 2, 3, 1, 2, 2 ]

    import time
    start_time = time.time()
    print(solution(players, performance))   # return 2

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
