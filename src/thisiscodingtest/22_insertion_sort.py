"""
[LINK] https://www.youtube.com/watch?v=DRkL5EBZ7KY&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=22
[REF]
[TITLE] [이것이 코딩 테스트다 with Python] 22강 삽입 정렬
"""

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break

    print(array)


def main():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    import time
    start_time = time.time()
    insertion_sort(array)

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
