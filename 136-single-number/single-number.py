from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       
        count = Counter(nums)
        unique_values = []
        for key, value in count.items():
            if value == 1:
                unique_values.append(key)


        return min(unique_values)

        