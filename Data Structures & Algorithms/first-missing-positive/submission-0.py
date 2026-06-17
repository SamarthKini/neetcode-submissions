class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        to_ = max(nums)
        from_ = min(nums)
        if from_ < 1: 
            from_ = 1
        if to_ < 1: 
            to_ = 1
        if from_ > 1:
            return 1

        for i in range(from_, to_ + 1):
            if i not in nums:
                return i 
        return to_ + 1
