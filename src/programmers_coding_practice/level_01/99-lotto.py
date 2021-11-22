"""
:link:
:ref:
"""

def solution(lottos, win_nums):
    lottery = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1,
    }

    count_zero = 0
    count_match = 0
    for num in lottos:
        if num == 0:
            count_zero += 1
        if num in win_nums:
            count_match += 1

    return [lottery[count_match + count_zero], lottery[count_match]]

def main():
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))

if __name__ == "__main__":
    main()
