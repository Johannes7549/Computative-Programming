class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        missing_number = 0
        
        nums.sort()
        count = 0
        if n == 1:
            if nums[0] == 0:
                missing_number = 1
            else:
                missing_number = 0
        else:
            for i in range(n):
                if nums[i] != i:
                    missing_number = i
                    count +=1 
                    break
            if count == 0:
                missing_number = n

        return missing_number
    
            
            