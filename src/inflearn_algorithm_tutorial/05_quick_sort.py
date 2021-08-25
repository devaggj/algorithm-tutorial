# 퀵 정렬은 '분할 정복' 알고리즘으로 평균 속도가 O(N * logN) 이다.

# 피벗값을 하나 정해서 데이터를 두 집합으로 분류한다
# 피벗값은 기준으로 왼쪽에서 오른쪽으로, 오른쪽에서 왼쪽으로 읽어간다

# 왼쪽에서 오른쪽으로 읽어갈 때는, 피벗값보다 큰 것을 선택
# 오른쪽에서 왼쪽으로 읽어갈 때는, 피벗값보다 작은 것을 선택
# 큰 값과 작은값이 서로 엇갈리면 교체

def quick_sort(list, start, end):
    
    if start >= end: # 원소가 1개인 경우
        return 

    pivot = start # 키는 첫번째 원소
    L = start + 1
    R = end
    
    # 엇갈릴 때까지 반복
    while L <= R:
        # 키 값보다 큰 값을 만날 때까지 반복
        while L <= end and list[L] <= list[pivot]:
            L += 1
    
        # 키 값보다 작은 값을 만날 때까지 반복
        while R > start and list[R] > list[pivot]:
            R -= 1
    
        # 현재 작은값의 index와 큰값의 index가 엇갈린 상태면 키 값과 교체
        if L > R:
            temp = list[R]
            list[R] = list[pivot]
            list[pivot] = temp
        # 
        else:
            temp = list[R]
            list[R] = list[L]
            list[L] = temp
    
    print(list)
    quick_sort(list, start, R - 1)
    quick_sort(list, R + 1, end)
        
    
    
arr = [3, 7, 8, 1, 5, 9, 6, 10, 2, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
