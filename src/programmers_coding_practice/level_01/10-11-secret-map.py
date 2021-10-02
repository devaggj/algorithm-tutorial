"""
:link: https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
"""

def solution(n, arr1, arr2):
    
    # _arr1 = list(map(lambda x: bin(x)[-n:], arr1))
    # _arr2 = list(map(lambda x: bin(x)[-n:], arr2))
    # union = list(zip(_arr1, _arr2))
    # for a, b in union:
    
    answer = []
    for _1, _2 in zip(arr1, arr2):
        union = bin(_1 | _2)[2:]
        if len(union) < n:
            union += "0" * (n - len(union))
        union = union.replace("1", "#").replace("0", " ")
        # union = union.replace("0", " ")
        answer.append(union)
    return answer


def main():
    N = 5
    array1 = [9, 20, 28, 18, 11]
    array2 = [30, 1, 21, 17, 28]
    print(solution(N, array1, array2))
    
if __name__ == "__main__":
    main()