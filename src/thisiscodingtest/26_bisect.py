"""
[LINK] https://www.youtube.com/watch?v=-Gx0T92-7h8&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=26&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF]
[TITLE] 파이썬 이진 탐색 라이브러리
"""

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))    # return 2
print(bisect_right(a, x))   # return 4


array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)

    return right_index - left_index

print(count_by_range(array, 4, 4))  # return 2
print(count_by_range(array, -1, 3))  # return 6
