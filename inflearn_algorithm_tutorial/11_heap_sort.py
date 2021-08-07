
def heap_sort(length, list):
    
    # 데이터 구조를 힙으로 바꿈
    def heapify(num, heap):
        
        for i in range(1, num):
            child = i;
            do = True
            while do:   # while child != 0
                root = (child - 1) // 2
                if heap[root] < heap[child]:
                    heap[root], heap[child] = heap[child], heap[root]
                child = root
                
                if child == 0:
                    do = False
        
    # 실제 힙정렬
    def sort(num, heap):
        
        # 트리의 크기를 줄여가며 반복적으로 힙을 구성
        for i in range(num - 1, -1, -1):
            # 힙 상태의 트리는 root가 가장 큰 값이므로 트리의 가장 마지막 노드로 보내줌
            heap[0], heap[i] = heap[i], heap[0]
            
            root = 0
            child = 1   # this line of code may not be necessary
            do = True
            while do:   # while child < i
                #  자식 중에 더 큰 값을 찾기
                child = 2 * root + 1
                if child < i - 1 and heap[child] < heap[child + 1]:
                    print("child:", child, ", i:", i)
                    child += 1  # 오른쪽이 왼쪽보다 클 경우 오른쪽 값으로 child를 지정
                
                # root보다 child 노드값이 더 크다면 교환
                if child < i and heap[root] < heap[child]:
                    heap[root], heap[child] = heap[child], heap[root]
                
                root = child
                
                if child >= i:
                    do = False

    heapify(length, list)
    sort(length, list)                    
    return list


if __name__ == "__main__":
    length = 9
    list = [7, 6, 5, 8, 3, 5, 9, 1, 6]
    print(heap_sort(length, list))
