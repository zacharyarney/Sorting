### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
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


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) / 2 ] )
        right = merge_sort( arr[ len( arr ) / 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
# based on C solution at: https://www.geeksforgeeks.org/in-place-merge-sort/ 
def merge_in_place(arr, start, mid, end):
    # TO-DO
    start2 = mid + 1
  
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]):
        return arr
  
    # Two pointers to maintain start 
    # of both arrays to merge 
    while start <= mid and start2 <= end:
  
        # If element 1 is in right place 
        if arr[start] <= arr[start2]:
            start += 1 
        
        else:
            value = arr[start2]
            index = start2
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            
            arr[start] = value
  
            # Update all the pointers 
            start += 1
            mid += 1
            start2 += 1
    
    return arr
        
  
# l is for left index and r is right index of the  
# sub-array of arr to be sorted 
def merge_sort_in_place(arr, l, r): 
    if l < r:
  
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) / 2
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
  
        merge_in_place(arr, l, m, r)

    return arr


# TO-DO: implement the Quick Sort function below
def quick_sort( arr, low, high ):
    # base case
    if high-low <= 0:
        return arr

    # partition
    pivot = low
    for i in range(low+1, high+1):
        if arr[i] < arr[pivot]:
            # move to LHS of pivot - 2 swaps
            temp = arr[i]
            arr[i] = arr[pivot+1]
            arr[pivot+1] = temp

            temp = arr[pivot]
            arr[pivot] = arr[pivot+1]
            arr[pivot+1] = temp
            pivot += 1
    
    # Quick Sort LHS, RHS
    arr = quick_sort(arr, low, pivot-1)
    arr = quick_sort(arr, pivot+1, high)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    # see source code at: https://github.com/python/cpython/blob/master/Objects/listobject.c
    return arr