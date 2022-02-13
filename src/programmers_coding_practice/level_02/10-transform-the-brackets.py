"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
[REF] https://latte-is-horse.tistory.com/151
[TITLE] 괄호 변환
"""

def seperation(w):
    count, idx = 0, 0
    for i, each in enumerate(w):
        if each == "(": count += 1
        else: count -= 1

        if count == 0:
            idx = i + 1
            break

    return w[:idx], w[idx:]

def isComplete(_u):
    if _u[0] == ")":
        return False

    count = 0
    for each in _u:
        if each == "(": count += 1
        else: count -= 1

        if count < 0:
            return False

    return False if count else True

def solution(p):
    answer = ""
    if p == "":
        return answer

    u, v = seperation(p)

    if isComplete(u):
        answer = u + solution(v)
    else:
        answer += "(" + solution(v) + ")"
        u = u[1:-1]

        pair = {"(": ")", ")": "("}
        for each in u:
            answer += pair[each]

    return answer


def main():
    # p = "(()())()"  # return "(()())()"
    p = "()))((()"  # return "()(())()"

    import time
    start_time = time.time()
    print(solution(p))

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
