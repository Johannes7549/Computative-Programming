class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]  
        first_element = nums[0]
        rest_elements = nums[1:]


        rest_permutations = self.permute(rest_elements)

        all_permutations = []
        for perm in rest_permutations:
            for i in range(len(perm) + 1):
                new_permutation = perm[:i] + [first_element] + perm[i:]
                all_permutations.append(new_permutation)

        return all_permutations
