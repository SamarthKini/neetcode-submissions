class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        add, result = 0, 0
        count = {}
        count[0] = 1
        for num in nums:
            add += num
            # diff = add - k
            result += count.get(add-k, 0)

            count[add] = 1 + count.get(add, 0)
            # if count[k-add]:
        return result