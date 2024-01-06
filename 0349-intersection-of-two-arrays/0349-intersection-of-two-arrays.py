class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        intersection = []
        minimum = min(n,m)
        for i in range(minimum):
            if n>m:
                if nums2[i] in nums1 and nums2[i] not in intersection:
                    intersection.append(nums2[i])
            else:
                if nums1[i] in nums2 and nums1[i] not in intersection:
                    intersection.append(nums1[i])
                
        return intersection