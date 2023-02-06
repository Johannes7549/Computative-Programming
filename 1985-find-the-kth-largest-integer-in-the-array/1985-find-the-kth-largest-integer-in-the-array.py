class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = [int(i) for i in nums]
        arr.sort()
        return str(arr[len(nums) - k])
 
                
                
                
                