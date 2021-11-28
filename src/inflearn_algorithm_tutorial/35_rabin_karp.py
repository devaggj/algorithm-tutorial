"""
:link: https://www.youtube.com/watch?v=kJJQJDsjXc8&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=35&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
:ref: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ndb796&logNo=221240679247
"""

def findString(parent, pattern):
    parentSize = len(parent)
    patternSize = len(pattern)

    parentHash = 0
    patternHash = 0
    power = 1

    for i in range(0, parentSize - patternSize + 1):
        if i == 0:
            for j in range(0, patternSize):
                parentHash = parentHash + ord(parent[patternSize - 1 - j]) * power
                patternHash = patternHash + ord(pattern[patternSize - 1 - j]) * power

                if j < (patternSize - 1):
                    power = power * 2
        else:
            parentHash = 2 * (parentHash - ord(parent[i - 1]) * power) + ord(parent[patternSize - 1 + i])

        if parentHash == patternHash:
            finded = True
            for j in range(0, patternSize):
                if parent[i + j] != pattern[j]:
                    finded = False
                    break

            if finded:
                print(f'{i + 1}번째에서 발견했습니다.')


def main():
    parent = "ababacabacaabacaaba"
    pattern = "abacaaba"
    findString(parent, pattern)

    return 0

if __name__ == "__main__":
    main()
