class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s:str, left:int, right:int) -> bool:
            while left < right:
                if s[right] != s[left]:
                    return False
                left += 1
                right -= 1
            return True
        # check = False
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if is_palindrome(s, left+1, right) or is_palindrome(s, left, right-1):
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True