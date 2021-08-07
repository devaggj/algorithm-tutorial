class InsertionSort():
    
    def insertion_sort(self):
        
        arr = [4, 7, 8, 5, 1, 3, 9, 2, 10, 6]
        min_temp = 0
        
        for i in range(0, len(arr) - 1):
            
            j = i
            while j >= 0 and arr[j] > arr[j + 1]:
                min_temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = min_temp
                j = j - 1

        print(arr)


if __name__ == '__main__':
    InsertionSort().insertion_sort()