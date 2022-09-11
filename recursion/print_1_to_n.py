# User function Template for python3

class Solution:

    def printTillN(self, N):
        # Base Condition : N == 1
        # Hypothesis : printTillN(n-1)
        # Induction : print(n)

        if N == 1:
            print(1, end=" ")
            return
        self.printTillN(N - 1)
        print(N, end=" ")
