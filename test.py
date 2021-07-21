def selection_sort():
    arr = [4, 7, 8, 5, 1, 3, 9, 2, 10, 6]
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(arr)

if __name__ == '__main__':
    selection_sort()
