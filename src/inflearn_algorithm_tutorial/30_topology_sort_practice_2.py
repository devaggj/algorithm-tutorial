MAX = 501

n = 0
inDegree = [ 0 for _ in range(0, MAX) ]
time = [ 0 for _ in range(0, MAX) ]
result = [ 0 for _ in range(0, MAX) ]
vector = [ [0] for _ in range(0, MAX) ]

def topology():
    
    queue = []
    
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            result[i] = time[i]
            queue.append[i]
    
    for _ in range(1, n + 1):
        x = queue.pop(1)
        
        for j in range(0, len(vector[x])):
            y = vector[x][j]
            result[y] = max(result[y], result[x] + time[y])
            inDegree[y] -= 1
            if inDegree[y] == 0:
                queue.append[y]
    
    for i in range(1, n + 1):
        print(result[i])
        

def main():
    n = 999
    for i in range(1, n + 1):
        t = 999
        time[i] = t
        while True:
            x = 999
            if x == -1: break
            inDegree[i] += 1
            vector.append[i]
    topology()
            
if __name__ == "__main__":
    main()
