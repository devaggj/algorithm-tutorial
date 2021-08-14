"""
계수정렬

범위 조건이 있는 정렬
조건에 맞는 수각 계수 후, 계수에 맞게 수를 나열하는 방식
:시간복잡도: O(N)
"""

def counting_sort(list):
    
    n = max(list) + 1
    count = [ 0 ] * n
    
    for i in range(0, len(list)):
        # count[list[i] - 1] += 1   # 기존 0이 없는 경우의 list
        count[list[i]] += 1
    
    sorted_list = []
    for i in range(0, n):
        if count[i] != 0:
            for j in range(0, count[i]):
                # sorted_list.append(i + 1) # 기존 0이 없는 경우의 list
                sorted_list.append(i) 
    
    return sorted_list



if __name__ == '__main__':
    
    example = [
        1, 3, 2, 4, 3, 2, 5, 3, 1, 2, 
        3, 4, 4, 3, 5, 1, 2, 3, 5, 2, 
        3, 1, 4, 3, 5, 1, 2, 1, 1, 1,
        0, 0
    ]
    print(counting_sort(example))