def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


arr = [5, 2, 1, 8, 9, 0, 6, 7, 3, 4]
bubble_sort(arr)
print(arr)

