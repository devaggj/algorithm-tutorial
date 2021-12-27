"""
:link: https://programmers.co.kr/learn/courses/30/lessons/17686?language=python3
:ref: https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%ED%8C%8C%EC%9D%BC%EB%AA%85-%EC%A0%95%EB%A0%AC-Python
"""

def solution(files):
    import re
    files_re = [ re.split(r"([0-9]+)", s) for s in files ]
    files_sorted = sorted(files_re, key=lambda x: (x[0].lower(), int(x[1][:5])))

    return [ "".join(each) for each in files_sorted ]



def main():
    import time

    s = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    start_time = time.time()
    print(solution(s))

    end_time = time.time()
    print("time:", end_time - start_time)


# execute
main()
