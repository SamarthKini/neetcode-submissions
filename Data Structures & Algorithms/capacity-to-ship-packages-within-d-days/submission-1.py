class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            days_taken = 1
            current = 0
            for weight in weights:
                if current+weight <= capacity:
                    current += weight
                else:
                    days_taken += 1
                    current = weight
            return days_taken <= days
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left+right)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left
            