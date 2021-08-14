def descending_sort(n):
    return int(''.join(sorted(str(n), reverse=True)))

if __name__ == '__main__':
    num = 118372
    print(descending_sort(num))
