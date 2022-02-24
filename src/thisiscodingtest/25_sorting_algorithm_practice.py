"""
[LINK] https://www.youtube.com/watch?v=_kdE7ykab4Q&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=25&ab_channel=%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4
[REF]
[TITLE] 정렬 알고리즘 비교 및 기초 문제 풀이 - 두 배열의 원소 교체
"""

n = 5
k = 3
aa = [1, 2, 5, 4, 3]
bb = [5, 5, 6, 6, 5]


def solution():
    aa.sort()
    bb.sort(reverse=True)

    for i in range(k):
        if aa[i] < bb[i]:
            aa[i], bb[i] = bb[i], aa[i]
        else:
            break

    print(sum(aa))


def main():

    import time
    start_time = time.time()
    solution()

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
