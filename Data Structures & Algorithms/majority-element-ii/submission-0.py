class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_holder = Counter(nums)
        maximum = -1
        output = []
        for num, count in count_holder.items():
            if count > len(nums) / 3:
                output.append(num)
        return output