class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        unique = []

        # Step 1: Collect unique elements
        for i in nums:
            if i not in unique:
                unique.append(i)

        
        k = len(unique)
        for i in range(k):
            nums[i] = unique[i]

        # Done: nums[:k] is the required unique part
        return k
