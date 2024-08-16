class Solution:
    """docstring for Solution"""

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i : i[0])
        outPut = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = outPut[-1][1]

            if start <= lastEnd:
                outPut[-1][1] = max(lastEnd, end)
            else:
                outPut.append([start, end])
        return outPut
        

ans = Solution()
l = [[1,3],[2,6],[8,10],[15,18]]
print(ans.merge(l))