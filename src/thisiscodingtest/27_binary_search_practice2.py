"""
[LINK] https://www.youtube.com/watch?v=jjOmN2_lmdk&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=27&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF]
[TITLE] 정렬된 배열에서 특정 수의 개수 구하기
"""


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    target_start = 0
    target_end = end

    for i in range(0, end + 1):
        if array[i] == target:
            target_start = i
            break
    else:
        target_start = -1

    for i in range(end, 0, -1):
        if array[i] == target:
            target_end = i
            break
    else:
        target_end = -int(1e9)

    return target_end - target_start + 1


def main():
    n = 7
    x = 2   # return 4
    array = [1, 1, 2, 2, 2, 2, 3]

    result = binary_search(array, x)
    
    if result > 0:
        print(result)
    else:
        print(-1)


### execute
main()
