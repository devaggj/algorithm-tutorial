import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = 6, 11
start = 1

visited = [False] * (n + 1)
distance = [INF] * (n + 1)


graph = [
    []
    ,[(2, 2), (3, 5), (4, 1)]
    ,[(3, 3), (4, 2)]
    ,[(2, 3), (6, 5)]
    ,[(3, 3), (5, 1)]
    ,[(3, 1), (6, 2)]
    ,[]
]


def dijkstar(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]

    while True:
        min_value = INF
        index = 0
        print("distance:", distance)
        for i in range(1, n + 1):
            if not visited[i] and distance[i] < min_value:
                print("i:", i)
                min_value = distance[i]
                index = i
        print("visited:", visited)
        if min_value == INF:
            break

        print("index:", index)
        visited[index] = True
        print("distance[index]:", distance[index])
        for j in graph[index]:
            cost = distance[index] + j[1]
            if cost < distance[j[0]]:
                print("j[0]:", j[0])
                distance[j[0]] = cost


def main():
    dijkstar(start)
    print("visited:", visited)
    print("distance:", distance)

###
main()
