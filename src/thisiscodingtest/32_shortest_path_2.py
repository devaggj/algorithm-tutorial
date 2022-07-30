"""

[TITLE] 미래 도시
"""


INF = int(1e9)

n = 5   # 도시 개수
m = 7   # 간선 개수

"""
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

distance = [
    (1, 2), (1, 3), (1, 4),
    (2, 4),
    (3, 4), (3, 5),
    (4, 5)
]

for each in distance:
    a, b = each
    graph[a][b] = 1
    graph[b][a] = 1

# x, k = map(int, input().split())
x, k = 4, 5

for k in range(1, n + 1):
    for i in range (1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = graph[1][k] + graph[k][x]

if answer >= INF:
    print("-1")
else:
    print(answer)   # return 3
