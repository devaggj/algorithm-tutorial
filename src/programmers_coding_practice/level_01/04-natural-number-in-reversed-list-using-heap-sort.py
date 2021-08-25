"""
reference: https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3

[NOTE] 힙 정렬을 이용했기에 항상 정렬된 형태로 뒤집혀서 return 함
원래 문제의 취지와는 좀 다른 방식
"""


def reversed_list(natural_number):
    
    list_stringified = list(map(lambda x: int(x), list(str(natural_number))))
    
    def heapify(list, index, heap_length):
        selected_root = index
        child_left = 2 * index + 1
        child_right = 2 * index + 2
        
        if child_left < heap_length and list[child_left] < list[selected_root]:
            selected_root = child_left
    
        if child_right < heap_length and list[child_right] < list[selected_root]:
            selected_root = child_right
        
        if selected_root != index:
            list[selected_root], list[index] = list[index], list[selected_root]
            heapify(list, selected_root, heap_length)
    
    
    def heap_sort(list):
        n = len(list)
        
        for i in range(n // 2 - 1, -1, -1):
            heapify(list, i, n)
    
        for j in range(n - 1, 0, -1):
            list[0], list[j] = list[j], list[0]
            heapify(list, 0, j)
        
        return list
    
    return heap_sort(list_stringified)


if __name__ == "__main__":
    n = 12345
    print(reversed_list(n)) # return [5,4,3,2,1]
