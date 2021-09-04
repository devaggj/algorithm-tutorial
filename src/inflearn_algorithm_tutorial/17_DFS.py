"""
ref: https://brownbears.tistory.com/558
"""

def depth_first_search(graph, root):
    visited = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    
    return stack


def main():
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
    
    
    print(depth_first_search(graph_list, root_node))

if __name__ == '__main__':
    main()