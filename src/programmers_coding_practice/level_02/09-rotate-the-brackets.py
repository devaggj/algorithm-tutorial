"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/76502?language=python3
[REF] https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B4%84%ED%98%B8-%ED%9A%8C%EC%A0%84%ED%95%98%EA%B8%B0
[TITLE] 괄호 회전하기
"""

from collections import deque

pair = {")": "(", "]": "[", "}": "{"}

def check_pair(brackets):
    stack = []
    for each in brackets:
        if each in "([{":
            stack.append(each)
        elif len(stack) > 0 and stack[-1] == pair[each]:
            stack.pop()
        else:
            return False
    else:
        if len(stack) == 0:
            return True

def solution(s):
    answer = 0
    deq = deque(s)

    for _ in range(len(s)):
        fob = deq.popleft()
        deq.append(fob)

        if check_pair(deq):
            answer += 1

    return answer


def main():
    s = "[](){}"

    import time
    start_time = time.time()
    print(solution(s))  # return 3

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
