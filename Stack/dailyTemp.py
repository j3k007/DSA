class Solution():
    def dailyTemperature(self, temperature:list[int]) -> list[int]:
        result = [0] * len(temperature)
        stack = []

        for i,temp in enumerate(temperature):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([temp, i])

        return result
    
ans = Solution()
listOfTemp = [73,74,75,71,69,72,76,73]
print(ans.dailyTemperature(listOfTemp))
