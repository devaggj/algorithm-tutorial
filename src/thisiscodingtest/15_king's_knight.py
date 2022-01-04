"""
:link: https://www.youtube.com/watch?v=QhMY4t2xwG0&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=15&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
:ref:
"""

'''시뮬레이션 유형'''
def solution(location):
    # 나이트가 이동할 수 있는 8가지 방향
    steps = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]
    row = int(location[1])
    column = int(ord(location[0])) - 97 + 1  # ord('a') -> 97

    # 8가지 방향에 대해 각 위치로 이동 가능한지 확인
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]

        if next_row < 1 or next_row > 8 or next_column < 1 or next_column > 8:
            continue

        result += 1

    return result


def main():
    location = 'a1'

    import time
    start_time = time.time()
    print(solution(location))   # return 2

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
