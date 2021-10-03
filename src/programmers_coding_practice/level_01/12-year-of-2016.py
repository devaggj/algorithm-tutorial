"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3
:ref: https://jhnyang.tistory.com/109
"""

# mathematical approach
def solution(a, b):
    datesInMonth = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    day = [ "THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED" ]
    sum = b
    for i in range(1, a):
        sum += datesInMonth[i-1]
    return day[sum % 7]
    # return day[(sum(datesInMonth[:a-1]) + b) % 7]

# repetitive aspect
def solution2(a, b):
    datesInMonth = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    day = [ "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU" ]
    
    target_month = a
    target_day = b
    
    _month = 1
    _day = 1
    sum = 0
    while target_month > _month or target_day > _day:
        _day += 1
        sum = (sum + 1) % 7
        
        if _day > datesInMonth[_month - 1]:
            _month += 1
            _day = 1
    
    return day[sum]

# mathematical approach 2
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
    print(solution2(mon, date))
    
if __name__ == "__main__":
    main()
