class Solutoin:
    def maxSubArr(self, nums) -> list[int]:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub
