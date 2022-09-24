class Solution:
    def isAlphaNumeric(self, c):  # 1
        return (ord("A") <= ord(c) <= ord("Z") or  # 2
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))

    def isPalindrome(self, s: str) -> bool:
        L = 0  # 3
        R = len(s) - 1  # 4

        while L < R:  # 5
            while not self.isAlphaNumeric(s[L]) and L < R:  # 6
                L += 1
            while not self.isAlphaNumeric(s[R]) and L < R:  # 7
                R -= 1
            if s[L].lower() != s[R].lower():  # 8
                return False
            else:  # 9
                L += 1
                R -= 1
        return True  # 10
