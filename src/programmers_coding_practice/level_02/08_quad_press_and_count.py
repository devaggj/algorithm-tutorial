"""
:link:
:ref1: https://donggoolosori.github.io/2020/12/19/pgmquad/
:ref2: https://drcode-devblog.tistory.com/189
"""

answer = [0,0]

def isBlock(length, y, x, arr):
    for i in range(y, y + length):
        for j in range(x, x + length):
            if arr[y][x] != arr[i][j]:
                return False
    return True

def quad(length, y, x, arr):
    if isBlock(length, y, x, arr):
        answer[arr[y][x]] += 1
        return

    center = length // 2
    quad(center, y, x, arr)
    quad(center, y, x+center, arr)
    quad(center, y+center, x, arr)
    quad(center, y+center, x+center, arr)

def solution(arr):
    quad(len(arr), 0, 0, arr)
    return answer


def main():
    # return [4,9]
    arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]

    import time
    start_time = time.time()
    print(solution(arr))

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
