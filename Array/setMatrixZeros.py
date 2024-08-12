class Solution:
    def setZeroes(self, matrix: list[list[int]])-> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        frow = False
        fcol = False

        # Check if there is 0 in first column, set fcol true
        for i in range(row):
            if matrix[i][0] == 0:
                fcol = True

        # Check if there is 0 in first row, set frow true
        for i in range(col):
            if matrix[0][i] == 0:
                frow = True

        # Check row elements (by ignoring first row and first column), If zero is found
        # set correponding row and col first element to zero.
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0


        # Check every row's first element starting from second row.
        # Set complete row to zero if zero is found.
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, col):
                    matrix[i][j] = 0

        # Check every column's first element starting from second column.
        # Set complete column to zero if zero is found.
        for j in range(1, col):
            if matrix[0][j] == 0:
                for i in range(1, row):
                    matrix[i][j] = 0

        # If fcol is true, set first column to zero
        if fcol:
            for i in range(row):
                matrix[i][0] = 0                

        # If frow is true, set first row to zero
        if frow:
            for i in range(col):
                matrix[0][i] = 0


