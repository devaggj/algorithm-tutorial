"""
:link: https://www.inflearn.com/course/algorithm-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8B%A4%EC%8A%B5/lecture/12354?tab=curriculum
:ref: 
"""

import sys

number = 6
INF = sys.maxsize    
visited = [ False ] * 6   # 방문한 노드
distance = [ 0 ] * 6  # 최단 거리

graph = [
            [ 0, 2, 5, 1, INF, INF ],
            [ 2, 0, 3, 2, INF, INF ],
            [ 5, 3, 0, 3, 1, 5 ],
            [ 1, 2, 3, 0, 1, INF ],
            [ INF, INF, 1, 1, 0, 2 ],
            [ INF, INF, 5, INF, 2, 0 ],
        ]

'''가장 최소 거리를 가지는 정점을 반환'''
def getSmallIndex():
    min = INF
    index = 0 
    for i in range(0, number):
        if distance[i] < min and visited[i] == False:
            min = distance[i]
            index = i
    return index


'''다익스트라 수행함수'''
def dijkstra(start):
    for i in range(0, number):
        distance[i] = graph[start][i]
    visited[start] = True
    
    for i in range(0, number - 2):  # why -2????? => 첫노드와 마지막노드를 제외
        current = getSmallIndex()
        visited[current] = True

        print("current: ", current)
        for j in range(0, 6):
            if visited[j] != True:
                print("j: ", j)
                if distance[current] + graph[current][j] < distance[j]:
                    print(distance[current])
                    print(graph[current][j])
                    print(distance[j])
                    distance[j] = distance[current] + graph[current][j]
    
    return distance


def main():
    s = 0   # 0 2 3 1 2 4
    print(dijkstra(s))
    
if __name__ == "__main__":
    main()
