class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # Save the topleft
                topLeft = matrix[top][l + i]

                # Move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move top left into top right
                matrix[top + i][r] = topLeft

            l += 1
            r -= 1
        
        return matrix

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
ans = Solution()
img = ans.rotate(matrix)
print(img)