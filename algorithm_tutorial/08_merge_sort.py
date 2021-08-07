# 병합 정렬은 대표적인 '분할 정복' 방법을 채택한 알고리즘
# O(N * logN) 의 시간복잡도
# 
# 병합 정렬은 하나의 큰 문제를 두 개의 작은 문제로 분할한 뒤에 각자 계산하고 나중에 합치는 방법
# 기본 아이디어는 => 정확히 반으로 나누고 나중에 정렬하는 것임
# 
# 병합 정렬은 퀵 정렬과 다르게 피벗 값이 없고 항상 반으로 나눈다는 특징
# 이 특징이 단계의 크기가 logN이 되도록 만들어줌


def merge_sort(list):
    
    sortedArr = []
    
    def merge(list, start, middle, end):
        
        i = start
        j = middle + 1
        k = start
        
        # 작은 순서대로 배열에 삽입
        while i <= middle and j <= end:
            if list[i] <= list[j]:
                sortedArr[k] = list[i]
                i += 1
            else:
                sortedArr[k] = list[j]
                j += 1
            k += 1
            
        # 남은 데이터 삽입
        if i > middle:
            for t in range(j, end + 1):
                sortedArr[k] = list[t]
                k += 1
        else:
            for t in range(i, middle + 1):
                sortedArr[k] = list[t]
                k += 1
        
        # 정렬된 배열을 삽입
        for i in range(start, len(list)):
            list[i] = sortedArr[i]
    
    def sort(list, start, end):
        if start < end:
            middle = (start + end) // 2
            
            sort(list, start, middle)
            
            sort(list, middle + 1, end)
            
            merge(list, start, middle, end)

    return sort(list, 0, len(list) - 1)


if __name__ == '__main__':
    example = [7, 6, 5, 8, 3, 5, 9, 1]
    print(merge_sort(example))
