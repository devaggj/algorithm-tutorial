"""
[LINK https://www.youtube.com/watch?v=jjOmN2_lmdk&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=27&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF]
[TITLE] 떡볶이 떡 만들기
"""


def binary_dduk(array, target):
    start = 0
    # end = max(array)
    end = int(1e9)  # 1e9 == 10억
    result = 0

    while start <= end:
        total = 0
        mid = (start+end) // 2

        for each in array:
            if each > mid:
                total += each - mid

        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result

def main():
    n = 4
    m = 6
    array = [19, 15, 10, 17]

    result = binary_dduk(array, m)
    print(result)

###
main()
