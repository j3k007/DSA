# class Solution:
#     def maxProduct(self, nums: list[int]) -> int:
#         maxSub = nums[0]
#         currProd = nums[0]

#         for n in nums:
#             if n > 0:
#                 currProd *= n
#             # elif n <= 0:
#             #     continue
#             maxSub = max(maxSub, currProd)
#         return currProd
    

# arr = [9, 2, -3, -4, 5]
# # arr = [-2, 0, -1]
# ans = Solution()
# print(ans.maxProduct(arr))

