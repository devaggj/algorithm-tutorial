"""
https://www.acmicpc.net/problem/1181
"""

def compare(num1, num2):
    
    if len(num1) < len(num2):
        return 1
    elif len(num1) > len(num2):
        return 0
    else:   # 길이가 같은 경우
        return num1 < num2
    
def vocabulary_sort(arr):
    
    n = len(arr)
    
    vocab_list = list(set(arr))
    vocab_list.sort(key = lambda x, y: x < y)
    
    for each in vocab_list:
        print(each)
    
    

if __name__ == "__main__":
    example  = [
        'but', 'i', 'wont', 'hesitate', 'no', 
        'more', 'no', 'more', 'it', 'cannot', 
        'wait', 'im', 'yours'
    ]
    vocabulary_sort(example)


"""
words_num = int(input())
words_list = []

for _ in range(words_num):
    word = str(input())
    word_count = len(word)
    words_list.append((word, word_count))

#중복 삭제
words_list = list(set(words_list))

#단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))

for word in words_list:
    print(word[0])
"""