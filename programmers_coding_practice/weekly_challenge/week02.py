"""
https://programmers.co.kr/learn/courses/30/lessons/83201?language=python3
"""

def solution(scores):
    
    scores_transposed = list(map(list, zip(*scores)))
    
    size = len(scores)
    for i in range(0, size):
        
        self_score = scores_transposed[i][i]
        
        scores_transposed[i][i] = -1
        largest = max(scores_transposed[i])
        
        scores_transposed[i][i] = 101
        smallest = min(scores_transposed[i])
    
        if smallest <= self_score and self_score <= largest:
            scores_transposed[i][i] = self_score
    
    avg = []
    for j in range(0, size):
        n = size
        total = 0
        for k in range(0, size):
            if scores_transposed[j][k] > 100:
                n -= 1    
            else:
                total += scores_transposed[j][k]
        avg.append(total / n)

    grade = ""        
    for t in range(0, size):
        if 90 <= avg[t]: grade = grade + "A"
        elif 80 <= avg[t] and avg[t] < 90: grade = grade + "B"
        elif 70 <= avg[t] and avg[t] < 80: grade = grade + "C"
        elif 50 <= avg[t] and avg[t] < 70: grade = grade + "D"
        else: grade = grade + "F"
        
    return grade


if __name__ == '__main__':
    records = [
                [100,90,98,88,65],
                [50,45,99,85,77],
                [47,88,95,80,67],
                [61,57,100,80,65],
                [24,90,94,75,65]
            ]
    print(solution(records))
