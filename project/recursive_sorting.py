# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first
    # element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# Define pivot (high in this case)
# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort(arr, low, high):
    pivot = low
    swapper = pivot
    if low < high:
        for i in range(low+1, high+1):
            if arr[i] < arr[pivot]:
                swapper += 1
                arr[i], arr[swapper] = arr[swapper], arr[i]

        arr[pivot], arr[swapper] = arr[swapper], arr[pivot]

        quick_sort(arr, low, swapper)
        quick_sort(arr, swapper+1, high)
    return arr


test_arr = [3, 5, 8, 4, 2, 9, 6, 0, 1, 7]
quick_sort(test_arr, 0, len(test_arr)-1)

# STRETCH: implement the Timsort function below
# hint: check out
# https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
