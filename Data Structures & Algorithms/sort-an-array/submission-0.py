class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 1:
            return nums
        mid = length//2
        left = nums[:mid]
        right = nums[mid:]
        left = self.sortArray(left)
        right = self.sortArray(right)
        l, r, i = 0, 0, 0
        len_left = len(left)
        len_right = len(right)
        output = [0] * length
        while l < len_left and r < len_right:
            if left[l] < right[r]:
                output[i] = left[l]
                l += 1
            else:
                output[i] = right[r]
                r += 1
            i += 1
        while l < len_left:
            output[i] = left[l]
            l += 1
            i += 1
        while r < len_right:
            output[i] = right[r]
            r += 1
            i += 1
        return output
        


