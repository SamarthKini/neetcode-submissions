class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            nums = list(set(nums))
            nums.sort()
        else:
            return 0
        max_count = 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i]  == nums[i-1] + 1:
                temp += 1
                max_count = max(temp, max_count)
            else:
                temp = 1
        return max_count
