"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3
"""

def solution(arr, divisor):
    answer = sorted([ i for i in arr if i % divisor == 0 ] )
    return answer if len(answer) else [ -1 ]


def main():
    array = [5, 9, 7, 10]	
    div = 5
    print(solution(array, div))
    
if __name__ == "__main__":
    main()