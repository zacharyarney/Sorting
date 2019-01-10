# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
  # loop through n-1 elements
  for i in range(1, len(arr)):
    temp = arr[i]
    j = i
    while j > 0 and temp < arr[j - 1]:
      # shift left until correct position found
      arr[j] = arr[j - 1]
      j -= 1
    # insert at correct position
    arr[j] = temp

  return arr