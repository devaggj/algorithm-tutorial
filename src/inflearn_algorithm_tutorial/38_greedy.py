"""
:link: https://www.youtube.com/watch?v=PNPIk3hc6ic&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=38&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
:ref: https://m.blog.naver.com/ndb796/221242106787
"""

def greedy(number):
    result = 0

    result += number // 500
    number %= 500

    result += number // 100
    number %= 100

    result += number // 50
    number %= 50

    result += number // 10

    return result


def main():
    number = 1260
    print(greedy(number))

if __name__ == "__main__":
    main()
