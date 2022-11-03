# Python implementation of Insertion Sort
def insertionSort(arr):
	# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them 
            arr[j],arr[j+1] = arr[j+1], arr[j]
            # tmp = arr[j + 1]
            # arr[j + 1] = arr[j]
            # arr[j] = tmp
            j -= 1
    return arr

arr = [2,4,3,1,5,8]
print(insertionSort(arr))