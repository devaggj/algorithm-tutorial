"""
[LINK] https://www.youtube.com/watch?v=CJiF-muKz30&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=19&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF]
[TITLE] 19강 BFS 알고리즘
"""

from collections import deque

def bfs(graph, node, visited):
    queue = deque([node])

    # 현재 노드를 방문 처리
    visited[node] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")

        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def main():
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    node = 1
    visited = [False] * 9   # 각 노드가 방문된 정보를 표현 (1차원 리스트)

    import time
    start_time = time.time()
    bfs(graph, node, visited)

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
