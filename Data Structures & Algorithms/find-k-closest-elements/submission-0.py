class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # i = 1
        # count = 0
        # output = []
        # if x in arr:
        #     output.append(x)
        #     count += 1
        # while count < k:
        #     if x-i in arr and count < k:
        #         output.append(x-i) 
        #         count += 1
        #     if x+i in arr and count < k:
        #         output.append(x+i)
        #         count += 1
        #     i+=1
        # return sorted(output)
        l, r = 0, len(arr)-k
        while l < r:
            m = (l+r)//2
            if x-arr[m] > arr[m+k]-x:
                l = m+1
            else:
                r = m
        return arr[l:l+k]