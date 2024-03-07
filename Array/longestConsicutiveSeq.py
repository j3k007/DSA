# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         count = 0
#         s = 0
#         n = len(nums)
#         if n == 0:
#             return 0
#         for i in nums:
#             s += 1
#             if s in nums:
#                 count += 1
#         return count
    
# arr = [0,3,7,2,5,8,4,6,0,1]
# ans = Solution()
# print(ans.longestConsecutive(arr))

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of the sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
arr = [0,3,7,2,5,8,4,6,0,1]
ans = Solution()
print(ans.longestConsecutive(arr))