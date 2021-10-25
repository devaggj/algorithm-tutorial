"""
:link: 
:ref: 
"""

def solution(n, lost, reserve):
    
    result = []
    
    # for l_student in lost:
    #     aaa = []
    #     idx = None
    #     for r_student in reserve:
    #         if l_student-1 == r_student or l_student+1 == r_student:
                
    for r_student in reserve:
        if r_student-1 in lost:
            lost.remove(r_student-1)
        elif r_student+1 in lost:
            lost.remove(r_student+1)
    
    return n - len(lost)




def main():
    s = ""
    print(solution(s))
    
if __name__ == "__main__":
    main()
