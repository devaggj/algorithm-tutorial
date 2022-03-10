"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
[REF]
[TITLE] 가장 큰 수
"""

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [ x for x in tail if x > pivot ]
    right_side = [ y for y in tail if y <= pivot ]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


def solution(numbers):
    numbers = [ str(each) for each in numbers ]
    numbers = quick_sort(numbers)

    for i in range(0, len(numbers) - 1):
            prev, next = numbers[i], numbers[i+1]
            if prev + next < next + prev:
                numbers[i] = next
                numbers[i+1] = prev

    # numbers

    return str(int(''.join(numbers)))


def main():
    # numbers = [6, 10, 2]            # return "6210"
    numbers = [3, 30, 34, 5, 9]     # return "9534330"
    print(solution(numbers))


###
main()
