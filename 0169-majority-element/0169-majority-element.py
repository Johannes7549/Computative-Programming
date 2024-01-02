class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        count = 0
        
        nums.sort()
        answer_dict= {}
        
        for i in range(len(nums)):
            if nums[i] not in answer_dict:
                answer_dict[nums[i]] = 1
            else:
                answer_dict[nums[i]] = answer_dict[nums[i]] + 1
        
        greater_value = 0
        greater_key = 0
        for key,values in answer_dict.items():
            if values > greater_value:
                greater_value = values
                greater_key = key
                
                
    
        return greater_key
        