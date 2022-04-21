"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3
[REF] https://developnote.tistory.com/26
[REF] https://minhamina.tistory.com/58
[TITLE] 삼각 달팽이
"""


def solution(n):
    triangle = [[0 for _ in range(i+1)] for i in range(n)]

    x, y = -1, 0
    value = 1

    for i in range(n):
        for j in range(i, n):

            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            triangle[x][y] = value
            value += 1

    answer = []
    for level in triangle:
        for each in level:
            answer.append(each)

    print("triangle:", triangle)
    print(sum(triangle, []))
    return answer


def main():
    n = 4
    # return [1,2,9,3,10,8,4,5,6,7]

    print(solution(n))


###
main()
