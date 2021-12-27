"""
:link:
:ref:
"""

def solution(msg):

    answer = []
    dic = { chr(i + 64) : i for i in range(1, 27) }
    stream = 27

    i = 0
    w, c = 0, 1
    s = ""
    while i < len(msg):
        w = msg[i]
        s += w
        print(s)

        if s in dic:
            answer.append(dic[s])
            i += 1
        else:
            # print("[NEW]")
            dic[stream] = s
            stream += 1
            s = ""
            i = c
            c += 1

    return answer


def main():
    import time

    msg = "KAKAO"   # return [11, 1, 27, 15]
    start_time = time.time()
    print(solution(msg))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
