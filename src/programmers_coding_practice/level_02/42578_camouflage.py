"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
[REF] https://coding-grandpa.tistory.com/88
[TILE] 해시 > 위장
"""


def solution(clothes):
    hash_comb = {}
    for item, ctgr in clothes:
        hash_comb[ctgr] = hash_comb.get(ctgr, 0) + 1

    cart = 1
    for each in hash_comb:
        cart *= hash_comb[each] + 1

    return cart - 1


def main():
    # return 5
    clothes = [
        ["yellowhat", "headgear"],
        ["bluesunglasses", "eyewear"],
        ["green_turban", "headgear"]
    ]
    print(solution(clothes))


###
main()
