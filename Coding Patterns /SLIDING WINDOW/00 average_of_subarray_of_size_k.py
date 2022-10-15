# Average Of Sub-Array of Size K
# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

arr = [-10, 10, 20, 30, 40, 50, 60, 70, 80]
k = 5


def avg_sub_array(arr, k):
    wSum = 0
    wStart = 0
    ans = []

    for wEnd in range(len(arr)):
        wSum += arr[wEnd]
        if wEnd >= (k - 1):  # Tip: We use if in Fixed Window Size
            ans.append(wSum / k)
            wSum -= arr[wStart]
            wStart += 1

    return ans


print(avg_sub_array(arr, k))
