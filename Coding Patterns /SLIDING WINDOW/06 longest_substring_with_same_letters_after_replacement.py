# Longest Substring with Same Letters after Replacement (hard)

# Problem Statement #
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

# Example 2:
# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

# Example 3:
# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

String = "aabccbb"
K = 2

# String = "abbcb"
# K = 1

# String = "abccde"
# K = 1


def substring_with_same_letters_after_replacement(String, K):
    wStart = 0
    store = {}
    maxLength = 0

    maxFrequency = 0
    for wEnd in range(len(String)):
        rightChar = String[wEnd]

        # Storing the frequency of the characters
        if rightChar not in store:
            store[rightChar] = 1
        else:
            store[rightChar] += 1

        # Dynamic change of window size
        maxFrequency = max(maxFrequency, store[rightChar])
        # Window Length - Max Frequency will tell how many characters we have to replace inside the window and if that exceeds K then  we need to shrink the sliding window
        while (wEnd - wStart + 1) - maxFrequency > K:
            leftChar = String[wStart]
            store[leftChar] -= 1
            wStart += 1                                 # Window Shrink

        maxLength = max(maxLength, wEnd - wStart + 1)
    return maxLength


print(substring_with_same_letters_after_replacement(String, K))
