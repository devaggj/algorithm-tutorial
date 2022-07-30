"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3
[REF] https://velog.io/@tiiranocode/Python-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8A%9C%ED%94%8C
[TITLE] 튜플
"""


def solution(s):
    # listOfTuple = [set(each.split(',')) for each in s[1:-1]]
    # print(listOfTuple)



    for each in s[1:-1]:
        print(each.split('},'))



    aa = sorted([each.split(',') for each in s[2:-2].split('},{')], key=len)
    answer = []

    for each in aa:
        for num in each:
            if int(num) not in answer:
                answer.append(int(num))
                break

    return answer


def main():
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"     # return [2, 1, 3, 4]
    print(solution(s))


###
main()
