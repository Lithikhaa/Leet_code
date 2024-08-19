class Solution(object):
    def rotate(self, nums, k):
        if len(nums) == 0:
            return []
        if k == 0:
            return nums
        if len(nums)<k:
            nums[:] = Solution.rotate(self,nums,len(nums))
            nums[:] = Solution.rotate(self,nums,k-len(nums))
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums
            