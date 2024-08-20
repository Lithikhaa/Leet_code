class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
              """
        k = k % len(nums)
        sub = len(nums) - k
        nums[:] = nums[sub:] + nums[:sub]
        return nums