
class BubbleSort():
    
    def bubble_sort(self):
    
        min_temp = 0
        arr = [4, 7, 8, 5, 1, 3, 9, 2, 10, 6]
        
        for i in range(0, len(arr)):
            for j in range(0, len(arr) - 1 - i):
                if arr[j] > arr[j+1]:
                    min_temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = min_temp

        print(arr)



if __name__ == '__main__':
    BubbleSort().bubble_sort()
