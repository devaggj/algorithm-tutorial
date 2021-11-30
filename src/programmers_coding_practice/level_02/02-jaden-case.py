"""
:link: https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3
:ref:
"""

def solution(s):

    jadenCase = ''
    for character_set in s.split(' '):
        first = True
        for alphabet in character_set:
            if first and alphabet.isalpha():
                alphabet = alphabet.upper()
            elif alphabet.isalpha():
                alphabet = alphabet.lower()
            jadenCase += alphabet
            first = False
        jadenCase += ' '

    return jadenCase[:-1]



def main():
    s = "3people unFollowed me"

    # should print "3people Unfollowed Me"
    print(solution(s))


if __name__ == "__main__":
    main()
