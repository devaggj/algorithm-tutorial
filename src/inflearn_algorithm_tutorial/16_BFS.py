"""
ref: https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
ref: https://brownbears.tistory.com/556
"""

from collections import deque

def breadth_first_search(graph, root):
    visited = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            # queue += graph[node] - set(visited)
            queue.extend(graph[node])
    
    return visited









def main():
    # graph_list = {
    #     1: set([2, 3]),
    #     2: set([1, 3, 4, 5]),
    #     3: set([1, 2, 6, 7]),
    #     4: set([2, 5]),
    #     5: set([2, 4]),
    #     6: set([3, 7]),
    #     7: set([3, 6]),
    # }
    graph_list = {
        1: [2, 3],
        2: [1, 3, 4, 5],
        3: [1, 2, 6, 7],
        4: [2, 5],
        5: [2, 4],
        6: [3, 7],
        7: [3, 6],
    }
    root_node = 1
    
    print(breadth_first_search(graph_list, root_node))

if __name__ == '__main__':
    main()