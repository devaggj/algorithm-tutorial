"""
:link: https://www.youtube.com/watch?v=puH2p1CQEg4&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=14&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
:ref:
"""

def solution(n, input_direction):
    move_types = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0)
    }
    x, y = 1, 1

    for each in input_direction:
        move = move_types[each]
        nx = x + move[0]
        ny = y + move[1]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x, y = nx, ny

    return x, y


def main():
    n = 5
    input_direction = 'RRRUDD'

    import time
    start_time = time.time()
    print(solution(n, input_direction)) # return (3, 4)

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
