"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/87377?language=python3
[REF]
[TITLE] 교점에 별 만들기
"""

import sys

def cross_point(line1, line2):
    a, b, e = line1
    c, d, f = line2

    denom = a * d - b * c
    if denom == 0:
        return None

    x_coord = (b * f - e * d) / denom
    y_coord = (e * c - a * f) / denom

    if x_coord % denom or y_coord % denom:
        return None

    return (x_coord, y_coord)

def solution(line):
    '''
    1 직선들의 모든 교점을 구해서 collection으로 만들기
        1-1 교점 중에서 좌표의 최대/최솟값 구하기
    2 좌표의 최대값/최솟값으로 그리드 초기화
    3 별 print
    '''

    length = len(line)
    coordinates = set()
    default_int = sys.maxsize

    x_max = -default_int
    x_min = default_int
    y_max = -default_int
    y_min = default_int

    for i in range(0, length-1):
        for j in range(1, length):
            coord = cross_point(line[i], line[j])
            if coord:
                coordinates.add(coord)

    x_max = max([ each[0] for each in coordinates ], key=lambda x: x)
    x_min = min([ each[0] for each in coordinates ], key=lambda x: x)
    y_max = max([ each[1] for each in coordinates ], key=lambda y: y)
    y_min = min([ each[1] for each in coordinates ], key=lambda y: y)

    answer = ['.' * (x_max - x_min + 1)] * (y_max - y_min + 1)


    return answer


def main():
    line = [
        [2, -1, 4],
        [-2, -1, 4],
        [0, -1, 1],
        [5, -8, -12],
        [5, 8, 12]
    ]

    import time
    start_time = time.time()
    print(solution(line))

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
