class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1)
        check_left = Counter(s1)
        check_right = Counter(s2[:right])
        while right < len(s2):
            if check_right == check_left:
                return True
            check_right[s2[left]] -= 1
            left += 1
            check_right[s2[right]] += 1
            right += 1

        return check_right == check_left
