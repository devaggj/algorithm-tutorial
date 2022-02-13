"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/92334
[REF]
[TITLE] 신고 결과 받기
"""

'''
{
    muzi    : [apeach],
    frodo   : [muzi, apeach],
    apeach  : [],
    neo     : [frodo, muzi]
}
'''

from collections import defaultdict

def solution(id_list, report, k):

    result = defaultdict(int)
    for each in id_list:
        result[each] = 0

    history = defaultdict(list)
    report = list(set(report))

    for each in report:
        history[each.split(" ")[1]].append(each.split(" ")[0])
        
    for id in history:
        if len(history[id]) >= k:
            for email in history[id]:
                result[email] += 1

    return [ result[id] for id in result ]


def main():
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    import time
    start_time = time.time()
    print(solution(id_list, report, k))

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
