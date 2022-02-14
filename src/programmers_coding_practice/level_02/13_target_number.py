"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
[REF] https://velog.io/@timointhebush/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%83%80%EA%B2%9F-%EB%84%98%EB%B2%84-DFS-BFS-Python
[REF] https://jjnooys.medium.com/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%83%80%EA%B2%9F-%EB%84%98%EB%B2%84-javascript-1d7983d423b5
[REF] https://eda-ai-lab.tistory.com/475
[TITLE] 타겟 넘버
"""

numbers = [1, 1, 1, 1, 1]
target = 3  # return 5
answer = 0

def dfs(depth, sum):
    global answer
    if depth == len(numbers):
        if sum == target:
            answer += 1
        return

    dfs(depth + 1, sum + numbers[depth])
    dfs(depth + 1, sum - numbers[depth])

def solution():
    global answer
    dfs(0, 0)
    return answer


def main():

    import time
    start_time = time.time()
    print(solution())

    end_time = time.time()
    print("time:", end_time - start_time)


### execute
main()
