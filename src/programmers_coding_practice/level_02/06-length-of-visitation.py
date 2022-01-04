"""
:link: https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3
:ref: https://velog.io/@tjdud0123/%EB%B0%A9%EB%AC%B8-%EA%B8%B8%EC%9D%B4
"""

def solution(dirs):
    vector = {
        'L': (-1, 0), 'R': (1, 0),
        'U': (0, 1), 'D': (0, -1)
    }
    memo = set()

    px, py = (0, 0)
    for move in dirs:
        v = vector[move]
        nx = px + v[0]
        ny = py + v[1]

        if nx < -5 or nx > 5 \
            or ny < -5 or ny > 5:
            continue

        memo.add((px, py, nx, ny))
        memo.add((nx, ny, px, py))
        px, py = nx, ny

    return len(memo) // 2


def main():
    dir1 = "ULURRDLLU"  # return 7
    dir2 = "LULLLLLLU"  # return 7

    import time
    start_time = time.time()
    print(solution(dir1))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
