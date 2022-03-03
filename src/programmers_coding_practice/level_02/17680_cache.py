"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3
[REF] https://velog.io/@tiiranocode/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BA%90%EC%8B%9C
[TITLE] [1차] 캐시
"""


def solution(cacheSize, cities):
    cacheMemory = []
    time = 0

    for city in cities:
        city = city.lower()
        # cache allocation
        if cacheSize:
            # cache hit
            if cacheMemory.count(city):
                cacheMemory.pop(cacheMemory.index(city))
                cacheMemory.append(city)
                time += 1
            # cache miss
            else:
                if len(cacheMemory) == cacheSize:
                    cacheMemory.pop(0)
                cacheMemory.append(city)
                time += 5
        # cache none
        else:
            time += 5

    return time


def main():
    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

    result = solution(cacheSize, cities)
    print(result)

###
main()
