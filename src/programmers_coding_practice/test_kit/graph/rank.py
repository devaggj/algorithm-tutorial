'''
link: https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
ref: https://summa-cum-laude.tistory.com/16
ref: https://ansohxxn.github.io/algorithm/floyd/
'''

def solution(n, results):
    graph = [ [0] * n for _ in range(n) ]
    for p1, p2 in results:
        graph[p1 - 1][p2 - 1] = 1
        graph[p2 - 1][p1 - 1] = -1
    
    for k in range(n):                  
        for i in range(n):              
            for j in range(n):          
                if i != k:
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1
        
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[i][j] == 1 or graph[j][i] == 1:
                cnt += 1
        if cnt == n - 1:
            ans += 1
    
    return ans

def main():
    n = 5
    r = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, r))
    
if __name__ == "__main__":
    main()
    