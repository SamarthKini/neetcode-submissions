class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        max_list = []
        i = 0
        j = len(height) - 1
        while i < j:

            max_vol = max(max_vol, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else: 
                j -= 1
        return max_vol