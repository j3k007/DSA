"""
Three Approaches :-
1. Using Recursion
2. Using Combinatorial Formula
3. Using Dynamic programing with 1D array
"""

#1. Using Recursion
# class Solution:
# 	def generate(self, numRows: int)-> list[list[int]]:
# 		if numRows == 0:
# 			return []

# 		if numRows == [1]:
# 			return [[1]]

# 		prevRows = self.generate(numRows - 1)
# 		newRows = [1] * numRows

# 		for i in range(1, numRows - 1):
# 			newRows[i] = prevRows[-1][i - 1] + prevRows[-1][i]

# 		prevRows.append(newRows)
# 		return prevRows


#2. Using Combinatorial Formula
# class Solution:
	# def generate(self, numRows: int)-> list[list[int]]:
	# 	result = []
	# 	if numRows == 0:
	# 		return result

	# 	first_row = [1]
	# 	result.append(first_row)

	# 	for i in range(1, numRows):
	# 		prev_row = result[i - 1]
	# 		curr_row = [1]

	# 		for j in range(1, i):
	# 			curr_row.append(prev_row[i - 1] + prev_row[j])

	# 		curr_row.append(1)
	# 		result.append(curr_row)

	# 	return result


#3. Using Dynamic programing with 1D array
class Solution:
	def generate(self, numRows: int)-> list[list[int]]:
		if numRows == 0:
			return []

		if numRows == 1:
			return [[1]]

		prev_rows = self.generate(numRows - 1)
		prev_row = prev_rows[-1]
		current_row = [1]

		for i in range(1, numRows - 1):
			current_row.append(prev_row[i - 1] + prev_row[i])

		current_row.append(1)
		prev_rows.append(current_row)

		return prev_rows


ans = Solution()
rows = 4
sol = ans.generate(numRows=rows)
print(sol)