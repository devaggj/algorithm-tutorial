"""
reference: https://github.com/TheAlgorithms/Python/blob/master/sorts/heap_sort.py

max hip

"""

def heapify(raw_list, index, heap_length):
    
    largest_idx = index;   # 초기 부모 인덱스의 설정
    left_idx = 2 * index + 1;
    right_idx = 2 * index + 2;
    
    # root로 선택된 노드의 값이 child node의 왼쪽값보다 작을 경우
    if left_idx < heap_length and raw_list[left_idx] > raw_list[largest_idx]:
        largest_idx = left_idx
        
    # root로 선택된 노드의 값이 child node의 오른쪽값보다 작을 경우
    if right_idx < heap_length and raw_list[right_idx] > raw_list[largest_idx]:
        largest_idx = right_idx
        
    # 새로 선택된 최대값을 부모 node로 옮겨주는 작업
    if largest_idx != index:
        raw_list[largest_idx], raw_list[index] = raw_list[index], raw_list[largest_idx]
        heapify(raw_list, largest_idx, heap_length);
    

def heap_sort(raw_list):
    
    """
    return: the same collection ordered by ascending
    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> heap_sort([])
    []
    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    
    n = len(raw_list);
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(raw_list, i, n)
    
    for i in range(n - 1, 0, -1):
        raw_list[0], raw_list[i] = raw_list[i], raw_list[0]
        heapify(raw_list, 0, i)

    return raw_list

    
if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(heap_sort(unsorted))
