"""
:link: https://www.youtube.com/watch?v=QhMY4t2xwG0&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=15&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
:ref:
"""

'''완전탐색 유형'''
def solution(string):
    result = []
    value = 0
    count_int = 0

    for each in string:
        # 알파벳인 경우 리스트에 append
        if each.isalpha():
            result.append(each)
        # 숫자는 따로 더하기
        else:
            count_int += 1
            value += int(each)
    # 알파벳 오름차순 정렬
    result.sort()

    # 숫자가 하나라도 있었을 경우 리스트 가장 뒤에 append
    if count_int > 0:
        result.append(str(value))

    return "".join(result)


def main():
    string1 = "K1KA5CB7" # return ABCKK13
    string2 = "AJKDLSI412K4JSJ9D"   # return ADDIJJJKKLSS20

    import time
    start_time = time.time()
    print(solution(string2))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
