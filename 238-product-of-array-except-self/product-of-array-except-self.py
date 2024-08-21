# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         mul = []
#         for i in range(len(nums)):
#             li = nums[:i] + nums[i+1:]
#             product = 1
#             # print(li)
#             for j in li:
                
#                 product = product * j
            
#             mul.append(product)
#         return mul
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_products = [1] * length
        right_products = [1] * length
        mul = []

        # Calculate the left products for each element
        for i in range(1, length):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # Calculate the right products for each element
        for i in range(length - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # Combine the left and right products
        for i in range(length):
            mul.append(left_products[i] * right_products[i])

        return mul
