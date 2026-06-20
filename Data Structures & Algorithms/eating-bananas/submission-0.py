class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        values = range(h, max(piles)+1)
        output = 0
        def check(number):
            out_value = 0
            for pile in piles:
                now = pile//number
                if pile//number < pile/number:
                    now+=1
                out_value+=now
            return out_value
        left, right = 1, max(piles)
        while left <= right:
            mid = (left+right)//2
            if check(mid) <= h:
                output = mid
                right = mid-1
            else:
                left = mid+1
        return left
        