class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        output = 0
        left, right = 0, len(people)-1
        while left <= right:
            if people[right]+people[left] <= limit:
                output += 1
                left += 1
                right -= 1
            else:
                output += 1
                right -= 1
        return output