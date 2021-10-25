"""
:link: https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
:ref: 
"""

def solution(answers):
    rtn = []
    pattern_1 = [1,2,3,4,5]             # 5
    pattern_2 = [2,1,2,3,2,4,2,5]       # 8
    pattern_3 = [3,3,1,1,2,2,4,4,5,5]   # 10
    
    scores = [0] * 3
    for i in range(len(answers)):
        if answers[i] == pattern_1[i % len(pattern_1)]: scores[0] += 1
        if answers[i] == pattern_2[i % len(pattern_2)]: scores[1] += 1
        if answers[i] == pattern_3[i % len(pattern_3)]: scores[2] += 1
    
    for i, each in enumerate(scores):
        if max(scores) == each: rtn.append(i + 1)
    
    return sorted(rtn)




def main():
    answers = [1,2,3,4,5]
    print(solution(answers))
    
if __name__ == "__main__":
    main()
