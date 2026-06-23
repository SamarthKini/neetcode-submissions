class Solution:
    def findMin(self, nums: List[int]) -> int:
        least = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < least:
                least = nums[i]
            # else:
        return least