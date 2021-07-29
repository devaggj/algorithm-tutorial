# 백준 N개의 수 정렬하기 2751번 문제
# 
# 최대 숫자의 갯수는 1,000,000개 까지일 경우 N(1<=N<=1,000,000)
# 
# 시간제한이 1초일 경우에는 대략 100,000,000(1억)건의 데이터 처리가 가능함
# 그러므로 1백만 x 1백만 = 1억 이라서 O(N^2)의 알고리즘을 풀면 에러
#
# O(N * logN)의 알고리즘으로 풀어야 가능함
# 이 경우에는 대략 20 x 1백만 = 2천만 정도가 되므로 조건을 충족함
# log(2)N=10이면 210=1024≈103이므로, log(2)N=20정도일 때 N≈106이다. 
#
# 퀵정렬, 병합정렬, 힙정렬 사용가능
# 퀵정렬은 경우에 따라 O(N^2) 의 성능을 보이므로 병합정렬, 힙정렬 사용가능

def quick_sort(list, start, end):
    
    if start >= end: 
        return
    
    # pivot = list[(start + end) // 2]
    pivot = start
    L = start + 1
    R = end
    
    while L <= R:
        while L <= end and list[L] <= list[pivot]:
            L += 1
        while R > start and list[R] >= list[pivot]:
            R -= 1

        if R < L:   # 엇갈린 경우
            list[R], list[pivot] = list[pivot], list[R]
        else:   # R > L
            list[R], list[L] = list[L], list[R]

    quick_sort(list, start, R - 1)
    quick_sort(list, R + 1, end)
    

arr = [3, 7, 8, 1, 5, 9, 6, 10, 2, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
