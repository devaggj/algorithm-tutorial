"""
:reference: https://programmers.co.kr/learn/courses/30/lessons/84512?language=python3

solution_00: TBD
solution_01: https://ye333.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4python-%EC%9C%84%ED%81%B4%EB%A6%AC-%EC%B1%8C%EB%A6%B0%EC%A7%80-5%EC%A3%BC%EC%B0%A8-%EB%AA%A8%EC%9D%8C-%EC%82%AC%EC%A0%84
solution_02: https://hello-backend.tistory.com/38
solution_03: https://blog.naver.com/PostView.naver?blogId=jinhan814&logNo=222488988156&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
"""

def solution_01(word):
    vowel = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    
    answer = len(word)
    init = ((((5 + 1) * 5) + 1) * 5 + 1) * 5 + 1
    for s in word:
        answer += init * vowel[s]
        init = (init - 1) // 5
    
    return answer 

def solution_02(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    init = 781
    answer = 0
    
    for i in range(len(word)):
        for j in range(5):
            if vowel[j] == word[i]:
                answer += 1 + (j * init)
        init = (init - 1) // 5
    
    return answer

def solution_03(word):
    answer, pattern = 0, [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += 'AEIOU'.find(word[i]) * pattern[i] + 1
    
    return answer

def solution_00(word):  # 등비수열을 응용
    answer = 0
    for i, each in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * 'AEIOU'.find(each) + 1
        
    return int(answer)

def solution_x(word):
    vowel = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    
    pattern = 781
    answer = 0
    for i in range(len(word)):
        answer += vowel[word[i]] * pattern + 1
        pattern = (pattern - 1 ) // 5
    
    return answer 


def main():
    w = 'EIO'   # should return 1189
    
    # print(solution_01(w))
    # print(solution_02(w))
    # print(solution_03(w))
    # print(solution_00(w))
    print(solution_x(w))
    

if __name__ == '__main__':
    main()