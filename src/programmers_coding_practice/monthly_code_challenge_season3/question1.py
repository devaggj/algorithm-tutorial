def solution(numbers):
    exp = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    return sum(each for each in exp if each not in numbers)
    # for each in numbers:
    #     print(each)
    #     if each not in exp:
    #         answer += each
    # return answer



if __name__ == '__main__':
    N = [1,2,3,4,6,7,8,0]
    # N = [5,8,4,0,6,7,9]
    
    print(solution(N))
    