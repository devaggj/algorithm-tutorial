"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
[REF] https://coding-grandpa.tistory.com/86
[TITLE] 해시 > 전화번호 목록
"""


def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True


def solution_hash(phone_book):
    hash_map = {}
    for each in phone_book:
        hash_map[each] = 1

    for number in phone_book:
        prefix = ""
        for num in number:
            prefix += num
            if prefix in hash_map and prefix != number:
                return False

    return True


def main():
    # phone_book = ["119", "97674223", "1195524421"]    # return False
    phone_book = ["123", "456", "789"]  # return True

    # solution(phone_book)
    print(solution_hash(phone_book))


###
main()
