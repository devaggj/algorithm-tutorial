"""
[LINK] https://www.youtube.com/watch?v=-Gx0T92-7h8&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=26&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF]
[TITLE] 26강 이진 탐색 알고리즘
"""


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start+end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


def main():
    n = 10
    target = 7
    array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    result = binary_search(array, target, 0, n-1)
    print(result + 1)

    result2 = binary_search2(array, target, 0, n-1)
    print(result2 + 1)

###
main()
