'''
파이썬 heapq 라이브러리는 Min Heap 방식으로 구현되어 있음
-> 우선순위가 낮은 순서로 정렬됨 (오름차순 힙 정렬)
시간복잡도: O(longN)
'''

import heapq

def heapsort(iterable):
    h = []
    min_heap_result = []
    max_heap_result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        min_heap_result.append(heapq.heappop(h))

    # max heap 구현
    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        max_heap_result.append(-heapq.heappop(h))

    return min_heap_result, max_heap_result


def main():
    array = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    result_min, result_max = heapsort(array)

    print(result_min, "\n", result_max)

###
main()
