"""
[LINK]
[REF]
[TITLE]
"""

def do_replace(brackets):
    if brackets == "":
        return True

    brackets = brackets.replace("()", "").replace("{}", "").replace("[]", "")

    for pair in ["()", "{}", "[]"]:
        if brackets.find(pair) > -1:
            do_replace(brackets.replace("()", "").replace("{}", "").replace("[]", ""))
        elif brackets == "":
            return True
        else:
            return False

def solution(s):
    tmp_s = s
    answer = 0
    if len(s) % 2 == 1:
        return answer

    for i in range(len(s)):
        if do_replace(tmp_s):
            answer += 1

        tmp_s = tmp_s[1:] + tmp_s[0]

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
