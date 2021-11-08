'''
link: https://www.inflearn.com/course/algorithm-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8B%A4%EC%8A%B5/lecture/12361?tab=note
'''

MAX = 101
vertex = [ [] for _ in range(0, MAX) ]
degree = [ 0 for _ in range(0, MAX) ]
completed = [ False for _ in range(0, MAX) ]

# return True if the matching is successful, else False
def dfs(x):
    
    # 연결된 모든 노드에 대해서 들어갈 수 있는 시도
    for i in range(0, len(vertex[x])):
        tried = vertex[x][i]
        
        # 이미 처리된 노드는 더 이상 볼 필요가 없음
        if completed[tried]:
            continue
        completed[tried] = True
        
        # 비어있거나 점유 노드에 더 들어갈 공간이 있는 경우
        if degree[tried] == 0 or dfs(degree[tried]):
            degree[tried] = x
            return True
    
    return False;


def main():
    vertex[1].append(1)
    vertex[1].append(2)
    vertex[1].append(3)
    vertex[2].append(1)
    vertex[3].append(2)
    
    n = 3
    count = 0
    for i in range(1, n + 1):
        if dfs(i):
            count += 1
    
    print(f'{count}개의 매칭이 이루어졌습니다.')
    for i in range(1, MAX):
        if degree[i] != 0:
            print(f'{degree[i]} -> {i}')
    
    return 0

if __name__ == "__main__":
    main()
    