"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3
:ref: 
"""

def solution(d, budget):
    result = 0
    d.sort()
    for each in d:
        if each <= budget:
            result += 1
            budget -= each
    return result
    


def main():
    dept = [1,3,2,5,4]
    b = 9
    print(solution(dept, b))
    
if __name__ == "__main__":
    main()
