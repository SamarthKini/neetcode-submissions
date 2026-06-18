class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i= len(nums1)-1
        # output = []
        while i >= 0:
            if m > 0 and n > 0:
                if nums1[m-1] > nums2[n-1]:
                    nums1[i] = nums1[m-1]
                    m-=1
                else:
                    nums1[i] = nums2[n-1]
                    n-=1
            elif m > 0:
                nums1[i] = nums1[m-1]
                m-=1
            elif n > 0:
                nums1[i] = nums2[n-1]
                n-=1
            i-=1
                
            # if one < m and two < n:
            #     if i%2 == 1:
            #         output.append(nums1[one])
            #         one += 1
            #     else:
            #         output.append(nums2[two])
            #         two += 1

            # elif one < m:
            #     output += nums1[one:m+1]
            # elif two < n:
            #     output += nums2[two:n+1]
            
            # i+=1
            
        # return output