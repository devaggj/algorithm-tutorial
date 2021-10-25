"""
:link: https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
:ref: 
"""

def solution(array, commands):
    # rtn = []
    # for c in commands:
    #     sliced = array[c[0]-1:c[1]]
    #     sliced.sort()
    #     rtn.append(sliced[c[2]-1])
    # return rtn
    
    return [ sorted(array[c[0]-1:c[1]])[c[2]-1] for c in commands ]




def main():
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
    print(solution(array, commands))
    
if __name__ == "__main__":
    main()
