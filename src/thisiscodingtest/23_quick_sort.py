"""
[LINK] https://www.youtube.com/watch?v=EuJSDghD4z8&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=23
[REF]
[TITLE] [이것이 코딩 테스트다 with Python] 23강 퀵 정렬
"""

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def pythonic_quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [ x for x in tail if x <= pivot ]
    right_side = [ y for y in tail if y > pivot ]

    return pythonic_quick_sort(left_side) + [pivot] + pythonic_quick_sort(right_side)


def main():
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    import time
    start_time = time.time()

    # general approach
    quick_sort(array, 0, len(array)-1)
    print(array)

    # pythonic approach
    print(pythonic_quick_sort(array))

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
