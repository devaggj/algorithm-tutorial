import sys 

number = 4
INF = sys.maxsize

arr = [
    [0, 5, INF, 8],
    [7, 0, 9, INF],
    [2, INF, 0, 4],
    [INF, INF, 3, 0]
]

def floydWarshall():
    # d = [ [0]*number for i in range(number) ]
    # for i in range(number):
    #     for j in range(number):
    #         d[i][j] = arr[i][j]
    
    d = arr
    '''k = 거쳐가는 노드'''
    for k in range(number):
        '''i = 출발 노드'''
        for i in range(number):
            '''j = 도착 노드'''
            for j in range(number):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    
    print(d)

def main():
    floydWarshall()
    
if __name__ == "__main__":
    main()
    