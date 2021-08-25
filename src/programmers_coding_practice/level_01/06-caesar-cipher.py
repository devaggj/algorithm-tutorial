"""
:reference: https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3

:ASCII printable characters:
A = 65  Z = 90
a = 97  z = 122
space(' ') = 32

:application:
ord('a') => 97
chr(97) => 'a'
"""


def caesar_cipher(string, n):
    ASCII_A = ord('A')
    ascii_a = ord('a')
    
    rsl = ''
    for each in string:
        if each.isupper():
            rsl += chr((ord(each) + n - ASCII_A) % 26 + ASCII_A)
        elif each.islower():
            rsl += chr((ord(each) + n - ascii_a) % 26 + ascii_a)
        else:
            rsl += each

    return rsl

if __name__ == '__main__':
    s = "a B z"
    n = 4
    
    print('solution_01:', caesar_cipher(s, n))
    # print('solution_02:', solution_02(N))