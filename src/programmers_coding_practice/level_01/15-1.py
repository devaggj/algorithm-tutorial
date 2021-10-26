"""
:link: 
:ref: 
"""

# def getDivisor(n):
#     divisors = []
#     for i in range(2, (n // 2 + 1)):
#         if n % i == 0:
#             divisors.append(i)
#     return sorted(divisors)[0]

# def solution(n):
#     x = n - 1
#     if x % 2 != 0:
#         x = getDivisor(x)
#     if int(pow(x, 0.5)) == pow(x, 0.5):
#         x = int(pow(x, 0.5))
#     return x

def solution(n):
    for i in range(2, 1000001):
        if n % i == 1:
            return i



def main():
    n = 12
    print(solution(n))
    
if __name__ == "__main__":
    main()
