"""
[LINK] https://www.youtube.com/watch?v=65Ui3RNibRA&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=25
[REF]
[TITLE] 계수 정렬

시간복잡도: O(N + K)
공간복잡도: O(N + K)
데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작
"""

def counting_sort(array):

    count = [0] * (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')


def main():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

    import time
    start_time = time.time()
    counting_sort(array)

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
