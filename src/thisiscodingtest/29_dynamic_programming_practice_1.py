"""
[LINK]
[REF]
[TITLE] 29강 다이나믹 프로그래밍 기초 문제 풀이
"""

'''개미 전사'''
def warrior_ant(n, array):
    memo = [0] * 100

    memo[0] = array[0]
    memo[1] = max(array[0], array[1])

    for i in range(2, n):
        memo[i] = max(memo[i - 1], memo[i - 2] + array[i])

    return memo[:n]


'''1로 만들기'''
def to_one(x):
    count = 1
    x -= 1

    while x != 1:
        if x % 5 == 0:
            x = x // 5
        elif x % 3 == 0:
            x = x // 3
        elif x % 2 == 0:
            x = x // 2

        count += 1

    return count


'''1로 만들기'''
def to_one_bottom_up(x):
    dp = [0] * 30001

    for i in range(2, x + 1):
        # 현재의 수에서 1을 빼는 경우
        dp[i] = dp[i - 1] + 1

        # 현재의 수가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        # 현재의 수가 3로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        # 현재의 수가 5로 나누어 떨어지는 경우
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)

    return dp[x]


def coin(coin_list, target_amount):
    # 화폐 단위 갯수
    coin_qty = len(coin_list)

    # dp 초기화
    dp = [10001] * (target_amount + 1)

    dp[0] = 0
    for i in range(coin_qty):
        for j in range(coin_list[i], target_amount + 1):
            # (i - k)원을 만드는 방법이 존재하는 경우
            if dp[j - coin_list[i]] != 10001:
                dp[j] = min(dp[j], dp[j - coin_list[i]] + 1)

    if dp[target_amount] == 10001:
        return -1
    else:
        return dp[target_amount]

    # result = 10001 if dp[coin_qty] == 10001 else dp[coin_qty]
    # return result


def main():

    '''개미 전사'''
    # n = 4
    # array = [1, 3, 1, 5]
    # print(warrior_ant(n, array))


    '''1로 만들기'''
    # x = 26
    # print(to_one(x))
    # print(to_one_bottom_up(x))


    '''효율적인 화폐 구성'''
    target_amount = 15
    coin_list = [2, 3]
    print(coin(coin_list, target_amount))   # return 5


###
main()
