# Fruits into Baskets (medium)
# "you can’t skip" in the question means its contiguous i.e substring or subarray

# Problem Statement #
# Given an array of characters where each character represents a fruit tree, you are given two baskets
# and your goal is to put maximum number of fruits in each basket. The only restriction is that each
# basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit
# from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# Example 2:
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

Fruit = ['A', 'B', 'C', 'A', 'C']

# Fruit = ['A', 'B', 'C', 'B', 'B', 'C']


def fruits_in_basket(Fruit, K=2):
    wStart = 0
    store = {}
    ans = 0

    for wEnd in range(len(Fruit)):
        rightFruit = Fruit[wEnd]
        if rightFruit not in store:
            store[rightFruit] = 1
        else:
            store[rightFruit] += 1

        while len(store) > K:
            leftFruit = Fruit[wStart]
            store[leftFruit] -= 1

            if store[leftFruit] == 0:
                del store[leftFruit]
            wStart += 1

        ans = max(ans, wEnd - wStart + 1)
    return ans


print(fruits_in_basket(Fruit))


# Time Complexity #
# The time complexity of the above algorithm will be O(N)O(N) where ‘N’ is the number of characters in the input array. The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N)O(N+N) which is asymptotically equivalent to O(N)O(N).

# Space Complexity #
# The algorithm runs in constant space O(1)O(1) as there can be a maximum of three types of fruits stored in the frequency map.
