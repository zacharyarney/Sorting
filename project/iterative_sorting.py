# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


my_arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(my_arr)
my_arr = selection_sort(my_arr)
print(f'INSERTION SORT {my_arr}')

# TO-DO: implement the Insertion Sort function below


def insertion_sort(arr):
    for i in range(1, len(arr)):
        currentvalue = arr[i]
        while i > 0 and arr[i-1] > currentvalue:
            arr[i] = arr[i-1]
            i = i-1
        arr[i] = currentvalue

    return arr


my_arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(my_arr)
my_arr = insertion_sort(my_arr)
print(f'INSERTION SORT {my_arr}')

# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):
    has_switched = True
    while has_switched:
        has_switched = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                has_switched = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

    return arr


my_arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(my_arr)
my_arr = bubble_sort(my_arr)
print(f'BUBBLE SORT {my_arr}')

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
