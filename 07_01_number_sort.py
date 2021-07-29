# 백준 수정렬하기 2750번 문제

import sys
import timeit

# %timeit

def number_sort(number):
    
    num_list = []
    for _ in range(0, number):
        num_list.append(int(input()))
    
    for i in range(0, number):
        min = sys.maxsize
        index = 0
        for j in range(i, number):
            if min > num_list[j]:
                min = num_list[j]
                idx = j
        
        temp = num_list[i]
        num_list[i] = min
        num_list[idx] = temp
    
    print(num_list)
    
    

N = int(input())
number_sort(N)
# timeit.timeit(number_sort(N))
