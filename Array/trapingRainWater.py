class Solution:
    def trap(self, height: list[int]):
        n = len(height) - 1
        r = [0] * n
        l = [0] * n
        ans = 0
        lm ,rm = 0, 0

        for i in range(n):
            l[i] = lm
            if lm < height[i]:
                lm = height[i]
            
        for i in range(n - 1, -1, -1):
            r[i] = rm
            if rm < height[i]:
                rm = height[i]

        for i in range(n):
            tarpped_water = min(l[i], r[i]) - height[i]
            if tarpped_water > 0:
                ans += tarpped_water
        
        return ans
    
ans = Solution()
a = [0,1,0,2,1,0,1,3,2,1,2,1]
print(ans.trap(a))