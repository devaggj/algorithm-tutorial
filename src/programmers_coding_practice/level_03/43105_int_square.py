'''
[LINK] https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
[REF] https://mjmjmj98.tistory.com/107
[REF] https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95-%EB%8F%99%EC%A0%81%EA%B3%84%ED%9A%8D%EB%B2%95
[TITLE] 정수 삼각형
'''

def solution(triangle):
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])

    return max(dp[-1])


def solution2(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])



def solution3(triangle):
    triangle = [[0] + each + [0] for each in triangle]
    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    print(triangle)
    return max(triangle[-1])



def main():
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    # result1 = solution(triangle) # return 30
    # print(result1)

    # result2 = solution2(triangle) # return 30
    # print(result2)

    result3 = solution3(triangle) # return 30
    print(result3)

###
main()
