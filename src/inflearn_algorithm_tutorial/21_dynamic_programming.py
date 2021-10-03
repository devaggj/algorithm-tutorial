memo = [ 0 for i in range(100)]
def dp(x):
    if x <= 2: return 1
    if memo[x] != 0: return memo[x]
    
    memo[x] = dp(x - 1) + dp(x - 2)
    return memo[x]
    


def main():
    # print(dp(10))
    print(dp(50))
    
if __name__ == "__main__":
    main()