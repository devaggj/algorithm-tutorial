"""
:link: https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3
:ref: https://minnit-develop.tistory.com/16
:ref: https://this-programmer.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Level1%ED%8C%8C%EC%9D%B4%EC%8D%AC3python3-%EC%95%BD%EC%88%98%EC%9D%98-%EA%B0%9C%EC%88%98%EC%99%80-%EB%8D%A7%EC%85%88
"""

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        divisor_cnt = 1
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                divisor_cnt += 1
        
        if divisor_cnt % 2 == 0:
            answer += i
        else: 
            answer -= i
    return answer

def solution2(left, right):
    answer = 0
    for i in range(left, right+1):
        '''제곱수의 약수의 개수는 홀수이고 제곱수가 아닌 경우는 짝수 성질 이용"'''
        if int(pow(i, 0.5)) == pow(i, 0.5):
            answer -= i
        else:
            answer += i
    return answer


def main():
    lt = 13
    rt = 17
    # print(solution(lt, rt))
    print(solution2(lt, rt))
    
if __name__ == "__main__":
    main()
