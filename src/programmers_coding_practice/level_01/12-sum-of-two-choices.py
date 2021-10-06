"""
:link: https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3
:ref: https://velog.io/@ckr3453/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%91%90-%EA%B0%9C-%EB%BD%91%EC%95%84%EC%84%9C-%EB%8D%94%ED%95%98%EA%B8%B0
"""

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    return sorted(answer)


from itertools import combinations
def solution2(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))
    return sorted(answer)


def main():
    num = [2,1,3,4,1]
    print(solution(num))
    
if __name__ == "__main__":
    main()
