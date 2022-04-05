"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/42626
[REF]
[TITLE] 더 맵게
"""

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        scale = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, scale)
        answer += 1

        if len(scoville) < 2 and scoville[0] < K:
            return -1

    return answer


def solution2(scoville, K):
    heapq.heapify(scoville)

    for i in range(1, 1000000):
        try:
            scale = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville, scale)
            if scoville[0] >= K:
                return i
        except:
            return -1


def main():
    scoville = [1, 2, 3, 9, 10, 12]  # return 2
    K = 7

    # print(solution(scoville, K))
    print(solution2(scoville, K))


###
main()
