"""
[LINK] https://www.youtube.com/watch?v=Ha0w2dJa2Nk&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=33&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF] https://freedeveloper.tistory.com/387
[TITLE] 32강 서로소 집합 자료구조
"""


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        # 루트 노드를 찾을 때까지 재귀 호출
        x = find_parent(parent, parent[x])
        return find_parent(parent, parent[x])
    return x


# 개선된 root노드 업데이트 함수
def find_parent_path_compression(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_path_compression(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent_path_compression(parent, a)
    b = find_parent_path_compression(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
# v, e = map(int, input().split())
v = 6
e = 4
parent = [0] * (v + 1)  # 부모 테이블 초기화하기
graph = [
    (1, 2), (1, 4),
    (2, 3),
    (5, 6)
]


# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i


# Union 연산을 각각 수행
for i in range(e):
    # a, b = map(int, input().split())
    a, b = graph[i]
    union_parent(parent, a, b)


# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v + 1):
    print(find_parent_path_compression(parent, i), end=' ')
print()


# 부모 테이블 내용 출력하기
print('부모 테이블: ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')
