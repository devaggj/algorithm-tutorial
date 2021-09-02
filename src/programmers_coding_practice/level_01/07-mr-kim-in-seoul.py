"""
:reference: https://programmers.co.kr/learn/courses/30/lessons/12919?language=python3
"""

def solution(seoul):
    answer = seoul.index('Kim')
    return f'김서방은 {answer}에 있다'

def main():
    seoul = ["Jane", "Kim"]
    
    print(solution(seoul))

if __name__ == '__main__':
    main()