"""
:link: https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3
:ref:
"""

def solution(people, limit):
    people.sort()

    count = 0
    weight = 0

    idx = 0
    while idx < len(people):
        weight += people[idx]
        idx += 1

        if weight < limit:
            continue
        else:
            weight = 0
            count += 1
            idx -= 1

    return count


def main():
    people = [70, 50, 80]
    limit = 100

    import time
    start_time = time.time()
    print(solution(people, limit))  # return 3

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
