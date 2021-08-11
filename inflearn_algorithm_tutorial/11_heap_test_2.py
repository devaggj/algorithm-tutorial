"""
This is a pure Python implementation of the heap sort algorithm.
For doctests run following command:
python -m doctest -v heap_sort.py
or
python3 -m doctest -v heap_sort.py
For manual testing run:
python heap_sort.py
"""


def heapify(unsorted, index, heap_size):
    
    smallest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    
    if left_index < heap_size and unsorted[left_index] < unsorted[smallest]:
        smallest = left_index

    if right_index < heap_size and unsorted[right_index] < unsorted[smallest]:
        smallest = right_index

    if smallest != index:
        unsorted[smallest], unsorted[index] = unsorted[index], unsorted[smallest]
        heapify(unsorted, smallest, heap_size)


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
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
        
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
        
    return unsorted


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(heap_sort(unsorted))
