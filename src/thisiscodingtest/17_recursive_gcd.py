"""
:link: https://www.youtube.com/watch?v=gFpKGWdEE5g&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=17
:ref:
"""

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def main():

    import time
    start_time = time.time()
    print(gcd(192, 162))    # return 6

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
