import collections
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 0:
            return []
        output = []
        left = right = 0
        q = collections.deque()

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()
            
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
            right += 1

        return output
    
ans = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3 
print(ans.maxSlidingWindow(nums=nums, k=k))       
