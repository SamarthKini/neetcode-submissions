class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        current = set()
        l, r = 0, 0
        while r < len(nums):
            if r-l > k:
                current.remove(nums[l])
                l+=1
            if nums[r] in current:
                return True
            else:
                current.add(nums[r])
                r+=1
        return False