"""
Time complexity: For Sorting then array O(nlogn) + 2 for loops O(n^2) = O(N^2).
Space complexity: O(N) one solution list is created.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, e in enumerate(nums):
            if i > 0 and e == nums[i - 1]:
                continue
            l , r =  i + 1, len(nums) - 1
            while l < r:
                threeSum = e + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([e, nums[l], nums[r]] )
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


arr = [-3, 3, 4, -3, 1, 2]
ans = Solution()
print(ans.threeSum(arr))
