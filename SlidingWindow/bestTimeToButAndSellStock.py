class Solution:
    def maxProfit(self, prices:list[int]):
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return maxProfit
    
ans = Solution()
prices = [2,1,4]
print(ans.maxProfit(prices))