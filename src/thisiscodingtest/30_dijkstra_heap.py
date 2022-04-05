'''
시간복잡도: O(ElogV)
E: 간선의 개수
V: 노드의 개수

직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가
모두 빼내는 연산과 매우 유사함
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
start = 1
n, m = 6, 11

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

graph_info = [
    []
    ,[(2, 2), (3, 5), (4, 1)]
    ,[(3, 3), (4, 2)]
    ,[(2, 3), (6, 5)]
    ,[(3, 3), (5, 1)]
    ,[(3, 1), (6, 2)]
    ,[]
]

graph = graph_info


def dijkstra(start):
    q = []

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        print("now:", now)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 (이미 가장 낮은 dist를 갱신했을 경우에 해당)
        if distance[now] < dist:
            print("distance[now]", distance[now],dist)
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                print("q:", q)
                print("distance:", distance)

def main():

    dijkstra(start)

    print("")
    print("graph:", graph)
    print("visited:", visited)
    print("distance:", distance)

    answer = []
    # 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(1, n + 1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if distance[i] == INF:
            # print("INFINITY")
            answer.append("INFINITY")
        else:
            # print(distance[i])
            answer.append(distance[i])

    print("각 노드로 가기 위한 최단 거리:", answer)

###
main()
