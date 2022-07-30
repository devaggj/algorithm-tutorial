"""
[LINK] https://www.youtube.com/watch?v=liuUazQaLuU&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=32&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[TITLE] 32강 최단 경로 알고리즘 기초 문제 풀이 - 전보
"""


import heapq
import sys

INF = int(1e9)
n, m = 3, 2
start = 1

graph = [[] for _ in range(n + 1)]
graph_info = [
    [],
    [(2, 4), (3, 2)],
    [],
    []
]
graph = graph_info

distance = [INF] * (n + 1)


def dijkstra(start):
    q = []

    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def main():
    dijkstra(start)

    count = 0
    max_travel = 0
    for dist in distance:
        if dist != INF:
            count += 1
            max_travel = max(dist, max_travel)

    print(count - 1, max_travel)ax_travel = 0
    for dist in distance:
        if dist != INF:
            count += 1
            max_travel = max(dist, max_travel)

    print(count - 1, max_travel)



###
main()



"""
3 2 1
1 2 4
1 3 2


2 4
"""