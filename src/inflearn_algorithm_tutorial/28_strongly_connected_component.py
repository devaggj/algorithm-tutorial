"""
:link: https://www.inflearn.com/course/algorithm-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8B%A4%EC%8A%B5/lecture/12357?tab=curriculum
:ref: 
"""

'''
정점(vertice) : 노드(node)라고도 하며 정점에는 데이터가 저장됩니다. (0, 1, 2, 3)
간선(edge): 링크(arcs)라고도 하며 노드간의 관계를 나타냅니다.
인접 정점(adjacent vertex) : 간선에 의해 연결된 정점으로 위에서 (정점0과 정점1은 인접 정점)
단순 경로(simple-path): 경로 중 반복되는 정점이 없는것, 같은 간선을 자나가지 않는 경로
차수(degree): 무방향 그래프에서 하나의 정점에 인접한 정점의 수 (정점 0의 차수는 3)
진출 차수(out-degree) : 방향그래프에서 사용되는 용어로 한 노드에서 외부로 향하는 간선의 수를 뜻합니다.
진입차수(in-degree) : 방향그래프에서 사용되는 용어로 외부 노드에서 들어오는 간선의 수를 뜻합니다.
'''



MAX = 10001


id = 0
degree = [ i for i in range(1, MAX) ]
finished = [False] * MAX        # 특정한 node에 대해 dfs가 끝났는지를 확인
adjacent = [0] * MAX            # 인접한 node들
SCC = []                        # 실질적 strongly connected component
stack = []


def dfs(x):
    # d[x] = ++id       # node마다 고유한 번호 할당
    stack.append(x)     # stack에 자기 자신 삽입
    
    parent = degree[x]      # 자기 자신이 부모가 됨
    # 인접한 node를 하나씩 확인
    for i in range(len(adjacent[x])):
        
        # y는 인접한 node 자체를 가리킴
        y = adjacent[x][i]
        
        # 만약에 해당 node를 방문한 적이 없다면, 해당 node로 dfs를 실행
        # 결과적으로 더 작은값으로 parent를 가리키게됨
        if degree[y] == 0: parent = min(parent, dfs(y))
        # 방문은 했지만, 아직 처리가 안된 node (현재 dfs를 수행하고 있는 node)
        # parent값을 처리되고 있는 값의 부모와 비교를 해서 더 작은값을 선택
        elif not finished[y]: parent = min(parent, degree[y])
        
        # parent node가 자기 자신인 경우
        if parent == degree[x]:
            scc = []
            while True:
                # top = stack[-1]
                # stack.pop()
                top = stack.pop()
                scc.append(top)
                finished[top] = True
                if top == x: break
            SCC.append(scc)

    # 자신의 부모값을 반환
    return parent


def main():
    # s = ""
    # print(solution(s))
    
if __name__ == "__main__":
    main()