"""
:link:
:ref:
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


def main():
    pattern = "abacaaba"
    table = makeTable(pattern)

    for i in range(0, len(table)):
        print(table[i])

if __name__ == "__main__":
    main()
