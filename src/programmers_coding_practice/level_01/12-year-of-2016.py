"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3
:ref: https://jhnyang.tistory.com/109
"""

def solution(a, b):
    datesInMonth = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    day = [ "THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED" ]
    sum = b
    for i in range(1, a):
        sum += datesInMonth[i-1]
    return day[sum % 7]
    # return day[(sum(datesInMonth[:a-1]) + b) % 7]

def solution2(a, b):
    
    return 0

def solution3(a, b):
    day = [ "THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED" ]
    sum = b
    for i in range(1, a):
        if i in [1, 3, 5, 7, 8, 10]:
            sum += 31
        elif i in [2]:
            sum += 29
        elif i in [4, 6, 9, 11]:
            sum += 30
    return day[sum % 7]


def main():
    mon = 5
    date = 24
    print(solution(mon, date))
    
if __name__ == "__main__":
    main()
