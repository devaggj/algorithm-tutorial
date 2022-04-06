"""
[LINK] https://www.youtube.com/watch?v=Mw8W56qNL8U&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=34&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF]
[TITLE] 34강 서로소 집합을 활용한 사이클 판별
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 필요 정보 설정 및 초기화
v = 3
e = 3
parent = [0] * (v + 1)  # 부모 테이블 초기화하기
graph = [
    (1, 2),
    (1, 3),
    (2, 3)
]
cycle = False


for i in range(1, v + 1):
    parent[i] = i


for i in range(e):
    a, b = graph[i]

    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다')


# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()


# 부모 테이블 내용 출력하기
print('부모 테이블: ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')
