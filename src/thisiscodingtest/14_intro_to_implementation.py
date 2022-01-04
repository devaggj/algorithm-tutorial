"""
:link: https://www.youtube.com/watch?v=puH2p1CQEg4&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=14&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
:ref:
"""

def vector_direction(dx, dy):
    # 현재위치
    x, y = 2, 2

    for i in range(len(dx)):
        # 다음위치
        nx = x + dx[i]
        ny = y + dy[i]
        print(nx, ny)

    return "[DONE]"


def main():
    # 현재위치에서 동 -> 북 -> 서 -> 남으로 움직인 경우
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    import time
    start_time = time.time()
    print(vector_direction(dx, dy))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
