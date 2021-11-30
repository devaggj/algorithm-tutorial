"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12949?language=python3
:ref: https://mathbang.net/562
:ref: https://wookcode.tistory.com/106
"""

def solution(arr1, arr2):

    # 2x3 3x2의 두 행렬일 경우 => 2x2의 행렬로 나옴
    result = [
        [ 0 for _ in range(len(arr2[0])) ] for _ in range(len(arr1))
    ]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            val = 0
            for k in range(len(arr1[0])):
                val += arr1[i][k] * arr2[k][j]
                result[i][j] = val

    return result


def main():
    arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    print(solution(arr1, arr2))


if __name__ == "__main__":
    main()



"""
array1 = [
    [2, 3, 2],
    [4, 2, 4],
    [3, 1, 4]
]

array2 = [
    [5, 4, 3],
    [2, 4, 1],
    [3, 1, 1]
]

result = [
    [22, 22, 11],
    [36, 28, 18],
    [29, 20, 14]
]
"""
