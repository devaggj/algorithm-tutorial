"""
:link:
:ref:
"""

def solution(s):

    '''
    1 ) 가 오면 false
    2 (의 갯수보다 )갯수가 많이지면 false
    3 (와 )의 갯수가 똑같아야 끝날 수 있음
    '''
    if s[0] == ")":
        return False

    count_open = 1
    count_close = 0
    for paren in list(s)[1:]:
        if count_open < count_close:
            return False
        
        if paren == '(':
            count_open += 1
        else:
            count_close += 1

    return count_open == count_close


def main():
    import time

    s = "(())()"    # return True
    start_time = time.time()
    print(solution(s))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
