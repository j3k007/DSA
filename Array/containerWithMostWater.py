"""
Time Complexity: O()
"""

class Solution:
    def maxArea(self, height:list[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height) - 1
        while (l < r):
            currArea = min(height[l],height[r]) * (r - l)
            maxArea = max(maxArea, currArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea

h = [1,8,6,2,5,4,8,3,7]
ans = Solution()
print(ans.maxArea(h))
