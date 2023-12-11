class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        position = 0
        for i in range(len(nums)):
            if nums[i] <= target:
                if nums[i] == target:
                    position = i
                    break
                else:
                    position = i+1
        return position
        