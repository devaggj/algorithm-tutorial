"""
:link: https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3
:ref:
"""

from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        deq = deque(skill)

        for each in tree:
            if each in deq:
                if each != deq.popleft():
                    break
        else:
            answer += 1

    return answer


def solution2(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        deq = deque(skill)

        for i, each in enumerate(tree):
            if each in deq:
                if deq.index(each) != 0:
                    break
                else:
                    deq.popleft()
            if i == len(tree) - 1:
                answer += 1

    return answer


def solution3(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        skt = "".join([ s for s in tree if s in skill ])

        if skill.find(skt) == 0:
            answer += 1

    return answer

def main():
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

    import time
    start_time = time.time()
    print(solution3(skill, skill_trees))     # return 2

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
