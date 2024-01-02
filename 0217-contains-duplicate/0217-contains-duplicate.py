class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        output = False
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                output = True
        return output