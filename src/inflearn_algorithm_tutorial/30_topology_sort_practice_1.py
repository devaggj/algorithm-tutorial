MAX = 32001

n = 0
inDegree = [ 0 for _ in range(0, MAX) ]
result = [ 0 for _ in range(0, MAX) ]
vector = [ [0] for _ in range(0, MAX) ]

def topologySort():
    
    queue = []
    
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)
    
    for i in range(1, n + 1):
        x = queue.pop(0)
        result[i] = x
        
        for j in range(0, len(vector[x])):
            y = vector[x][j]
            inDegree[y] -= 1
            if inDegree[y] == 0:
                queue.append(y)

    for i in range(1, n + 1):
        print(result[i])

def main():
    m = 999
    for i in range(0, m):
        x = 999
        y = 999
        vector[x].append[y]
        inDegree[y] += 1
    topologySort()

if __name__ == "__main__":
    main()
