"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/70129?language=python3
[REF]
[TITLE] 이진 변환 반복하기
"""


def solution(s):
    cnt_step = 0
    cnt_zero = 0

    while s != '1':
        cnt_zero = cnt_zero + s.count('0')
        s = s.replace('0', '')
        c = len(s)
        s = bin(c)[2:]

        cnt_step += 1

    return [cnt_step, cnt_zero]


def main():
    string = "110010101001"

    result = solution(string)
    print(result)


###
main()
