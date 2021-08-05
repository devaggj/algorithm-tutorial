#
# 
# 
# 


def merge_sort(list):
    
    sortedArr = []
    
    def sort(list, start, end):
        if start < end:
            middle = (start + end) // 2
            sort(start, middle)
            sort(middle, end)
            merge(list, start, middle, end)
    
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
            for t in range(j, end):
                sortedArr[k] = list[t]
                k += 1
        else:
            for t in range(i, middle):
                sortedArr[k] = list[t]
                k += 1
        
        # 정렬된 배열을 삽입
        list = sortedArr

    print(sort(list, 0, len(list) - 1))

# execution
example = [7, 6, 5, 8, 3, 5, 9, 1]
merge_sort(example)
