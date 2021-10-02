"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3
"""

def solution(arr):
    a = []
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]: a.append(arr[i-1])
    a.append(arr[-1]) 
    return a


def main():
    array = [1,1,3,3,0,1,1]     # return [1,3,0,1]
    # array = [4, 4, 4, 3, 3]     # return [4,3]
    print(solution(array))
    
if __name__ == "__main__":
    main()
