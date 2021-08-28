"""
:reference: https://programmers.co.kr/learn/courses/30/lessons/84325?language=python3#
:sorted-lambda 좋은 참조: https://rfriend.tistory.com/473
:sorted-tuple시에 좋은 참조: https://stackoverflow.com/questions/62748056/the-functools-cmp-to-key-isnt-working-on-this-comparison-of-two-tuple-problem

:key limitations:
# len(table) = 5
# 1 <= len(langueages) <= 9
# len(preference) = len(languages)
# 값이 같을 경우 사전순으로 return
"""

from functools import cmp_to_key

def solution(table, languages, preference):
    
    # [SUDO_CODE]
    # table의 문자열을 쪼개서 2차원의 배열로 만듦
    # 2차원 table에서 각각의 첫번째 index의 value를 key로 하고 value가 0인 return용 dictionary를 만듦
    
    # languages and preference를 zip으로 합쳐서 key, value 형태의 dictionary로 만듦
    # 2차원 table을 looping하며 각 언어점수의 합을 위에서 만든 return용 dictionary의 value에 넣음
    
    # return용 dict에서 value가 가장 높은 것의 key를 return
    
    new_table = [ string.split() for string in table ]
    result_dic = { f'{each[0]}' : 0 for each in new_table }
    lang_and_pref = dict(zip(languages, preference))
    
    score = len(new_table[0])
    for job_field in new_table:
        for key, value in lang_and_pref.items():
            for idx in range(1, len(job_field)):
                if key == job_field[idx]:
                    # print(key, job_field[idx])
                    result_dic[f'{job_field[0]}'] += value * (score - idx)
                    # print('score', score, 'idx', idx, 'value', value)
                    # print(value * (score - idx))

    test_print = {
        'new_table': new_table,
        'lang_and_pref': lang_and_pref,
        'score': score,
        'result_dic': result_dic 
    }
    
    return sorted(result_dic.items(), key=lambda x : (-x[1], x[0]))[0][0]
    # return sorted(result_dic.items(), key=cmp_to_key(kv_compare))[0][0]


def kv_compare(a, b):
    if a[1] != b[1]: 
        return b[1] - a[1]
    elif a[1] == b[1]:
        return -1 if a[0] < b[0] else 1
    return 0



def main():
    # [NOTE] should return "HARDWARE"
    # TABLE = [
    #     "SI JAVA JAVASCRIPTABLE SQL PYTHON C#", 
    #     "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
    #     "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
    #     "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", 
    #     "GAME C++ C# JAVASCRIPT C JAVA"
    # ]
    # l = [ "PYTHON", "C++", "SQL" ]
    # p = [7, 5, 5]
    
    # [NOTE] should return "PORTAL"
    TABLE = [
        "SI JAVA JAVASCRIPT SQL PYTHON C#", 
        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", 
        "GAME C++ C# JAVASCRIPT C JAVA"
    ]
    l = ["JAVA", "JAVASCRIPT"]
    p = [7, 5]
    
    print(solution(TABLE, l, p))


if __name__ == '__main__':
    main()