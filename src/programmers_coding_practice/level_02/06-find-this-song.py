"""
:link: https://programmers.co.kr/learn/courses/30/lessons/17683?language=python3#
:ref: https://json1995.tistory.com/entry/Python%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Level-2-%EB%B0%A9%EA%B8%88%EA%B7%B8%EA%B3%A1
"""

from datetime import datetime

def convert(melody):
    melody_converted = ''
    i = 1
    while i <= len(melody[:-1]):
        if melody[i] == '#':
            melody_converted += melody[i-1].lower()
            i += 2
        else:
            melody_converted += melody[i-1]
            i += 1

    if melody[-1] != '#':
        melody_converted += melody[-1]

    return melody_converted

def solution(m, musicinfos):
    m = convert(m)
    answer = { "title": "(None)", "time": 0 }

    for info in musicinfos:
        start_time, end_time, title, melody = info.split(',')

        start_time = datetime.strptime(start_time, "%H:%M")
        end_time = datetime.strptime(end_time, "%H:%M")

        hour_str, minute_str = str(end_time - start_time).split(':')[:-1]
        duration_minute = int(hour_str) * 60 + int(minute_str)

        melody = convert(melody)
        quotient, remainder = divmod(duration_minute, len(melody))
        melody_string = melody * quotient + melody[:remainder]
        print(melody_string)

        if m in melody_string:
            if answer["time"] < duration_minute:
                answer["title"] = title

    return answer["title"]


def main():
    import time

    m = "ABC"
    musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    start_time = time.time()
    print(solution(m, musicinfos))  # return "HELLO"

    end_time = time.time()
    print("time:", end_time - start_time)

# execute
main()
