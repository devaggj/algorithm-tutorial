"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/49189
[REF] https://whwl.tistory.com/268
[TITLE] 가장 먼 노드
"""

from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    visited[1] = 1
    queue = deque([1])

    while queue:
        node = queue.popleft()
        for link in graph[node]:
            if not visited[link]:
                visited[link] = visited[node] + 1
                queue.append(link)

    max_link = max(visited)
    cnt = visited.count(max_link)

    return cnt if cnt > 0 else 1


def main():
    n = 6
    vertex = [  # return 3
        [3, 6],
        [4, 3],
        [3, 2],
        [1, 3],
        [1, 2],
        [2, 4],
        [5, 2]
    ]
    print(solution(n, vertex))


###
main()
