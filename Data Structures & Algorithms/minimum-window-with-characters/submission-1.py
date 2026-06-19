class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        letter_check = {}
        for letter in t:
            letter_check[letter] = 1 + letter_check.get(letter, 0)
        output = ""
        needed = len(letter_check)
        have = 0
        output_check = {}
        while right < len(s):
            output_check[s[right]] = 1 + output_check.get(s[right], 0)
            if s[right] in letter_check and output_check[s[right]] == letter_check[s[right]]: 
                have += 1
            while have == needed:
                temp = s[left:right+1]
                if output == "" or right-left+1 < len(output):
                    output = temp
                if s[left] in letter_check:
                    output_check[s[left]] -= 1
                    if output_check[s[left]] < letter_check[s[left]]:
                        have -= 1
                left += 1
            right += 1
        
        return output

            
