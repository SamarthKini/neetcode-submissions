import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        in_string = re.sub(r'[^a-z0-9]', '', s.lower())   #"".join(s.lower())
        left, right = 0, len(in_string)-1
        while left < right:
            if in_string[left] != in_string[right]:
                return False
            left += 1
            right -= 1
            
        return True