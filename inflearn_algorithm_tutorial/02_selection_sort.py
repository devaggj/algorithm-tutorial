import sys

class SelectionSort():

    # def __init__(self):
        # self.min = sys.maxsize
        # self.idx = 0
        # self.temp = 0

    def selection_sort(self):
        min = sys.maxsize
        
        temp = 0
        arr = [4, 7, 8, 5, 1, 3, 9, 2, 10, 6]
    
        for i in range(0, len(arr) - 1):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min = arr[j]
                    min_idx = j
                    
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
            
        print(arr);

# def swap(self, arr, i, idx):
#   self.temp = arr[i]
#   arr[i] = arr[self.idx]
#   arr[self.idx] = self.temp

if __name__ == '__main__':
    SelectionSort().selection_sort()
