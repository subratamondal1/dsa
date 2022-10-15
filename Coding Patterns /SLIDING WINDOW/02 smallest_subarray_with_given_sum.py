# Smallest Subarray with a given sum (easy)

# Given an array of positive numbers and a positive number ‘S’, find the length of
# the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0,
# if no such subarray exists.

# op: 2

# arr = [2, 1, 5, 2, 3, 2]
# S = 7

# op: 1

arr = [2, 1, 5, 2, 8]
S = 7

# op: 3

# arr = [3, 4, 1, 1, 6]
# S = 8


def smallest_subarray(arr, S):
    wSum = 0
    wStart = 0
    ans = float("inf")

    for wEnd in range(len(arr)):
        wSum += arr[wEnd]

        while wSum >= S: # Tip: We use while loop in Variable Window Size
            wSum -= arr[wStart]
            ans = min((wEnd - wStart) + 1, ans)
            wStart += 1

    return ans


print(smallest_subarray(arr, S))
