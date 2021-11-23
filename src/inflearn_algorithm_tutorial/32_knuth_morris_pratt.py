"""
:link:
:ref: https://injae-kim.github.io/dev/2020/07/23/all-about-kmp-algorithm.html
"""

def makeTable(pattern):
    patternSize = len(pattern)
    table = [ 0 for _ in range(patternSize) ]
    j = 0
    for i in range(1, patternSize):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table

def KMP(parent, pattern):
    table = makeTable(pattern)
    print(table)
    parentSize = len(parent)
    patternSize = len(pattern)
    j = 0
    for i in range(0, parentSize):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == patternSize - 1:
                print(f"{i - patternSize + 2}번째에서 찾았습니다.")
                j = table[j]
            else:
                j += 1

def main_makeTable():
    pattern = "abacaaba"
    table = makeTable(pattern)

    for i in range(0, len(table)):
        print(table[i])

def main_KMP():
    parent = "ababacabacaabacaaba"
    pattern = "abacaaba"
    KMP(parent, pattern)

if __name__ == "__main__":
    # main_makeTable()
    main_KMP()
