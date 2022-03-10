"""
[LINK] https://www.youtube.com/watch?v=tWX6FZwwQMI&t=2140s&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF]
[TITLE] 29강 다이나믹 프로그래밍 기초 문제 풀이 - 금광
"""


for tc in range(int(input())):
    '''
    금광 정보 입력
    n -> 열, m -> 행
    '''
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 2차원 dp 테이블 초기화
    dp = []
    idx = 0

    for i in range(n):
        dp.append(array[idx:idx+m])
        idx += m

    for j in range(1, m):       # column
        for i in range(n):      # row
            # 왼쪽 위에서 오는 경우
            left_up = 0 if i == 0 else dp[i-1][j-1]

            # 왼쪽 아래에서 오는 경우
            left_down = 0 if i == n-1 else dp[i+1][j-1]

            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)
