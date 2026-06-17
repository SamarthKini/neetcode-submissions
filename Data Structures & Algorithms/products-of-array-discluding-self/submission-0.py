class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero += 1

        if zero == 0:
            return [product//num for num in nums]
        elif zero == 1:
            return [0 if num != 0 else product for num in nums]
        else:
            return [0]*len(nums)