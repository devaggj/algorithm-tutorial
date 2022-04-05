"""
[LINK] https://www.youtube.com/watch?v=hw-SvAR3Zqg&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=31&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF] https://freedeveloper.tistory.com/385
[TITLE] 31강 플로이드 워셜 알고리즘
"""

INF = int(1e9)

'''노드의 개수 및 간선의 개수를 입력받기'''
# n = int(input())
# m = int(input())
n = 4
m = 7

'''2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화'''
graph = [[INF] * (n + 1) for _ in range(n + 1)]

'''자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화'''
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

'''각 간선에 대한 정보를 입력 받아, 그 값으로 초기화'''
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c

distance = [
    (1, 2, 4), (1, 4, 6),
    (2, 1, 3), (2, 3, 7),
    (3, 1, 5), (3, 4, 4),
    (4, 3, 2)
]

for each in distance:
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c, = each
    graph[a][b] = c

'''점화식에 따라 플로이드 워셜 알고리즘을 수행'''
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

'''수행된 결과를 출력'''
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == 1e9:
            print("INFINITY", end="")
        else:
            print(graph[a][b], end=",")
    print()
