"""
:link: https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3
:ref:
"""

from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        deq = deque(skill)

        for i, s in enumerate(tree):
            if s == deq[0]:
                deq.popleft()

            if len(deq) == 0 or len(tree) - 1 == i and len(skill) - 1 > len(deq):
                answer += 1
                break

    return answer


def main():
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

    import time
    start_time = time.time()
    print(solution(skill, skill_trees))     # return 2

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
