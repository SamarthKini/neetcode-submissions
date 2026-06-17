class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_num = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != max_num:
                if count == 1:
                    max_num = nums[i]
                    continue
                count -= 1
            elif nums[i] == max_num:
                count += 1
        return max_num
