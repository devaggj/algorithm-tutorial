# 백준 3수정렬하기 2752번 문제

import sys
import timeit

# %timeit

def three_numbers_sort():
    
    num_list = []
    for _ in range(0, 3):
        num_list.append(int(input()))
    
    for i in range(0, 3):
        min = sys.maxsize
        index = 0
        for j in range(i, 3):
            if min > num_list[j]:
                min = num_list[j]
                idx = j
        
        temp = num_list[i]
        num_list[i] = min
        num_list[idx] = temp
    
    print(num_list)
    
    

three_numbers_sort()
# timeit.timeit(three_numbers_sort(N))
