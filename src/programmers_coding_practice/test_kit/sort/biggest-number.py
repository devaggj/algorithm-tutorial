"""
:link: https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
:ref: https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98
"""

def solution(numbers):
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))




def main():
    # arg = [6, 10, 2]
    arg = [0, 0, 0]
    print(solution(arg))
    
if __name__ == "__main__":
    main()
