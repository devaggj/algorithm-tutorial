"""
:link: https://www.inflearn.com/course/algorithm-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8B%A4%EC%8A%B5/lecture/12353?tab=curriculum
"""

def primeNumberSieve(number):
    
    # arr = [ 1 ] * number
    arr = list(range(number + 1))
    
    '''end = int(pow(number, 0.5)) + 1
    for i in range(2, end + 1):'''
    end = int(pow(number, 0.5)) + 1 + 1
    for i in range(2, end):
        if arr[i] == 0: continue
        for j in range(i + i, number, i):
            arr[j] = 0
    del arr[0]
    return arr


def main():
    num = 10
    print(primeNumberSieve(num))
    
if __name__ == "__main__":
    main()
