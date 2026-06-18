class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_diff = float('inf')
        current_sum = 0
        current_length = 0
        passed = False
        l = 0
        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                passed = True
                current_length = r-l+1
                min_diff = min(min_diff, current_length)
                # while current_sum >= target:
                current_sum -= nums[l]
                l+=1
        if passed:
            return min_diff
        else:
            return 0
