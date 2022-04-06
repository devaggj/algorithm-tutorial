"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/49191
[REF]
[TITLE] 순위
"""


def solution(n, results):
    graph = [[0] * n for _ in range(n)]

    for p1, p2 in results:
        graph[p1 - 1][p2 - 1] = 1
        graph[p2 - 1][p1 - 1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != k:
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1

    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if graph[i][j] == 1 or graph[j][i] == 1:
                count += 1

        if n - 1 == count:
            answer += 1

    return answer


def main():
    n = 5
    results = [     # return 2
        [4, 3],
        [4, 2],
        [3, 2],
        [1, 2],
        [2, 5]
    ]
    print(solution(n, results))

###
main()