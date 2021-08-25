"""
reference: https://github.com/TheAlgorithms/Python/blob/master/sorts/heap_sort.py
reference 2: https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/

This is a pure Python implementation of the heap sort algorithm.
For doctests run following command:
python -m doctest -v heap_sort.py
or
python3 -m doctest -v heap_sort.py
For manual testing run:
python heap_sort.py
"""


def heapify(unsorted, index, heap_size):
    
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    
    # root로 선택된 노드의 값과 child node의 왼쪽값 비교
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    # root로 선택된 노드의 값과 child node의 오른쪽값 비교
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    # 새로 선택된 값을 부모 node로 옮겨주는 작업
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)
        
    # smallest = index
    # left_index = 2 * index + 1
    # right_index = 2 * index + 2
    
    # if left_index < heap_size and unsorted[left_index] < unsorted[smallest]:
    #     smallest = left_index

    # if right_index < heap_size and unsorted[right_index] < unsorted[smallest]:
    #     smallest = right_index

    # if smallest != index:
    #     unsorted[smallest], unsorted[index] = unsorted[index], unsorted[smallest]
    #     heapify(unsorted, smallest, heap_size)


def heap_sort(unsorted):
    
    """
    Pure implementation of the heap sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> heap_sort([])
    []
    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    
    n = len(unsorted)
    
    # BUILD-MAX-HEAP (A) : 위의 1단계
    # 인덱스 : (n을 2로 나눈 몫-1)~0
    # 최초 힙 구성시 배열의 중간부터 시작하면 
    # 이진트리 성질에 의해 모든 요소값을 
    # 서로 한번씩 비교할 수 있게 됨 : O(n)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
        
    # Recurrent (B) : 2~4단계
    # 한번 힙이 구성되면 개별 노드는
    # 최악의 경우에도 트리의 높이(logn)
    # 만큼의 자리 이동을 하게 됨
    # 이런 노드들이 n개 있으므로 : O(nlogn)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0] # root 노드와 마지막 node 값 변경
        heapify(unsorted, 0, i)
        
    return unsorted



if __name__ == "__main__":
    
    # user_input = input("Enter numbers separated by a comma:\n").strip()
    # unsorted = [int(item) for item in user_input.split(",")]
    # print(heap_sort(unsorted))

    unsorted = [7, 6, 5, 8, 3, 5, 9, 1, 6]
    print(heap_sort(unsorted))
    