class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1
        selected = -1
        mid1 = 0
        while left <= right:
            mid1 = (left+right)//2
            if target <= matrix[mid1][-1] and target >= matrix[mid1][0]:
                selected = mid1
                break
            elif target > matrix[mid1][-1]:
                left = mid1+1
            elif target < matrix[mid1][0]:
                right = mid1-1
        if selected < 0:
            return False
        left, right = 0, len(matrix[mid1])
        while left <= right:
            mid2 = (left+right)//2
            if target == matrix[mid1][mid2]:
                return True
            elif target < matrix[mid1][mid2]:
                right = mid2-1
            elif target > matrix[mid1][mid2]:
                left = mid2+1
        return False
