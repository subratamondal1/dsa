# Maximum Sum Subarray of Size K (easy)

# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

arr = [2, 1, 5, 1, 3, 2]
k = 3


def max_sum_subarray_of_size_k(arr, k):
    wSum = 0
    wStart = 0

    ans = []

    for wEnd in range(len(arr)):
        wSum += arr[wEnd]
        # |0|1|2|
        if wEnd >= (k-1):  # Tip: We use if in Fixed Window Size
            ans.append(wSum)
            wSum -= arr[wStart]
            wStart += 1
    return max(ans)


print(max_sum_subarray_of_size_k(arr, k))
