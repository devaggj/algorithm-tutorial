"""
link: https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
"""

def solution(s):
    upper_case = []
    lower_case = []
    for each in s:
        if ord(each) < 93:
            upper_case.append(each)
        else:
            lower_case.append(each)
            
    return insertion_sort(lower_case) + insertion_sort(upper_case)

def insertion_sort(case):
    for i in range(len(case) - 1):
        j = i 
        while j >= 0 and case[j] < case[j + 1]:
            temp = case[j + 1]
            case[j + 1] = case[j]
            case[j] = temp
            j -= 1
    return "".join(case)


def main():
    S = "Zbcdefg"
    
    print(solution(S))

if __name__ == '__main__':
    main()