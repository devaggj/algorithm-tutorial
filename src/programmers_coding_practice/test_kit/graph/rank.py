'''
link: https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
ref: https://summa-cum-laude.tistory.com/16
'''

from collections import Counter

def solution(n, results):
    board = [ [0] * n for _ in range(n) ]
    for p1, p2 in results:
        board[p1 - 1][p2 - 1] = 1
        board[p2 - 1][p1 - 1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    if board[i][k] == 1 and board[k][j] == 1:
                        board[i][j] == 1
                    elif board[i][k] == -1 and board[k][j] == -1:
                        board[i][j] == -1

    ans = 0
    for i in range(n):
        if Counter(board[i])[0] == 1:
            ans += 1
    
    print(board)

def main():
    n = 5
    r = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    solution(n, r)
    
if __name__ == "__main__":
    main()
    