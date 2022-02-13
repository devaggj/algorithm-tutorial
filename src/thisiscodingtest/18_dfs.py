"""
[LINK] https://www.youtube.com/watch?v=1vLqC1rItM8&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=18
[REF]
[TITLE] 18강 DFS 알고리즘
"""

def dfs(graph, node, visited):

    # 현재 노드를 방문 처리
    visited[node] = True
    print(node, end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)


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
    dfs(graph, node, visited)

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
