class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        set_of_chars = set()
        n = len(s)
        for right in range(n):
            while s[right] in set_of_chars:
                set_of_chars.remove(s[left])
                left += 1
            set_of_chars.add(s[right])
            current_length = right - left + 1
            if current_length > longest:
                longest = current_length
        return longest
