from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maximum = Counter(nums)
        for key, value in maximum.items():
            maxelement,maxvalues = maximum.most_common(1)[0]
        return maxelement
    



        