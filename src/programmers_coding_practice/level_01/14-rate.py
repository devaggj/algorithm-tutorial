"""
:link: https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
:ref: 
"""

# from collections import defaultdict
def solution(N, stages):
    user_played = len(stages)
    rate = {}
    for i in range(N):
        rate.setdefault(i+1, 0)
    
    for stage in stages:
        if stage < N + 1:
            rate[stage] += 1

    for stage, user_failed in rate.items():
        rate[stage] = user_failed / user_played
        user_played -= user_failed
    
    return sorted(rate, key=lambda x: rate[x], reverse=True)
    


def main():
    n = 5
    s = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(n, s))  # return [3,4,2,1,5]
    
if __name__ == "__main__":
    main()
