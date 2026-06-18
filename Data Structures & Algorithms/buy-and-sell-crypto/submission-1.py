class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        l = 0
        for r in range(1, len(prices)):
            current = prices[r] - prices[l]
            if current > max_diff:
                max_diff = current
            if prices[r] < prices[l]:
                l = r

        return max_diff