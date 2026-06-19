class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = 0
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
        # if nums[mid] < target:
        #     return right+1
        # else:
        #     return max(left-1, 0)
        return left