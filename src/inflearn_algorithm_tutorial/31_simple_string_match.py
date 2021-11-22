"""
:link: https://www.inflearn.com/course/algorithm-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8B%A4%EC%8A%B5/lecture/12362?tab=curriculum
:ref: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ndb796&logNo=221240660061
"""


def findString(parent, pattern):
    parentSize = len(parent)
    patternSize = len(pattern)

    for i in range(0, parentSize - patternSize + 1):
        finded = True
        for j in range(0, patternSize):
            if parent[i + j] != pattern[j]:
                finded = False
                break;
        if finded:
            return i

    return -1


def main():
    parent = "Hello World"
    pattern = "llo W"
    result = findString(parent, pattern)

    if result == -1:
        print("찾을 수 없습니다.")
    else:
        print(f"{result + 1}번째에서 찾았습니다.")

if __name__ == "__main__":
    main()
