class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        newArray = []
        n = len(nums1)
        m = len(nums2)
        nPointer = 0
        median = 0
        mPointer = 0
        while nPointer<n and mPointer<m:
            if nums1[nPointer]<nums2[mPointer]:
                newArray.append(nums1[nPointer])
                nPointer += 1
            else:
                newArray.append(nums2[mPointer])
                mPointer+=1
        while nPointer<n:
            newArray.append(nums1[nPointer])
            nPointer+=1
        while mPointer<m:
            newArray.append(nums2[mPointer])
            mPointer+=1
        if (len(newArray)%2) == 0:
            median1 = (len(newArray)//2)-1
            median2 = median1+1
            median = (newArray[median1] + newArray[median2])/2
        else: 
            median = newArray[(len(newArray)-1)//2]
            
        return median