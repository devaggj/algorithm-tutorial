"""
[LINK] https://www.youtube.com/watch?v=tWX6FZwwQMI&t=2140s&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF]
[TITLE] 29강 다이나믹 프로그래밍 기초 문제 풀이 - 병사 배치하기
"""

# n = int(input())
# array = list(map(int, input().split()))
#
# array.reverse()



def longest_increasing_subsequence(n, array):
    array.reverse()
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return (n - max(dp))


def main():
    n = 7
    array = [15, 11, 4, 8, 5, 2, 4]
    print(longest_increasing_subsequence(n, array))

###
main()
