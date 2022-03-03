"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/87377?language=python3
[REF]
[TITLE] 교점에 별 만들기
"""


def cross_point(line1, line2):
    a, b, e = line1
    c, d, f = line2

    denom = a * d - b * c
    # 분모가 0 => 평행 혹은 일치
    if denom == 0:
        return None

    x_coord = (b * f - e * d) / denom
    y_coord = (e * c - a * f) / denom

    # if x_coord % denom != 0 or y_coord % denom != 0:
    #     print(x_coord % denom)
    #     return None

    # 교차점이 정수
    if x_coord == int(x_coord) and y_coord == int(y_coord):
        return (int(x_coord), int(y_coord))


def solution(line):
    '''
    1 직선들의 모든 교점을 구해서 collection으로 만들기
        1-1 교점 중에서 좌표의 최대/최솟값 구하기
    2 좌표의 최대값/최솟값으로 그리드 초기화
    3 별 print
    '''

    N = len(line)
    coordinates = set()
    # default_int = 1e9
    #
    # x_max = -default_int
    # x_min = default_int
    # y_max = -default_int
    # y_min = default_int

    for i in range(0, N-1):
        for j in range(i+1, N):
            coord = cross_point(line[i], line[j])
            if coord:
                coordinates.add(coord)

    # x_max = max([ each[0] for each in coordinates ], key=lambda x: x)
    # x_min = min([ each[0] for each in coordinates ], key=lambda x: x)
    # y_max = max([ each[1] for each in coordinates ], key=lambda y: y)
    # y_min = min([ each[1] for each in coordinates ], key=lambda y: y)

    x_coords = [ each[0] for each in coordinates ]
    x_max = max(x_coords)
    x_min = min(x_coords)

    y_coords = [ each[1] for each in coordinates ]
    y_max = max(y_coords)
    y_min = min(y_coords)


    # 좌표평면 그리기
    answer = ['.' * (x_max - x_min + 1)] * (y_max - y_min + 1)

    for coord in coordinates:
        x, y = coord

        modifed_line = list(answer[y_max - y])
        modifed_line[x - x_min] = '*'
        answer[y_max - y] = [ ''.join(point) for point in modifed_line ]

        # answer[y_max - y] = answer[y_max - y][:x - x_min] + "*" + answer[y_max - y][x - x_min + 1:]

    return [ ''.join(line) for line in answer ]

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
    answer = solution(line)
    print(answer)

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
