"""
link: https://programmers.co.kr/learn/courses/30/lessons/1845?language=python3
ref: 
"""

def solution(nums):
    return min(len(set(nums)), len(nums) / 2)




def main():
    n = [3,3,3,2,2,4]   # return 3
    print(solution(n))
    
if __name__ == "__main__":
    main()
