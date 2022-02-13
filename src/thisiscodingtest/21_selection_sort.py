"""
[LINK] https://www.youtube.com/watch?v=jpyslMwprao&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=21
[REF]
[TITLE] [이것이 코딩 테스트다 with Python] 21강 선택 정렬
"""

'''
시간복잡도 = O(N^2)
'''
def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]

    print(array)


def main():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    import time
    start_time = time.time()
    selection_sort(array)

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
