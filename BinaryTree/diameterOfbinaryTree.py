class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Define the recursive function to calculate diameter
        def diameter(node: TreeNode, res: list):
            if not node:
                # Base case: if the node is none, return 0
                return 0
            # Recurseviley calculate the diameter of left and right
            left = diameter(node.left, res)
            right = diameter(node.right, res)
            # Update the maximum diamtemer encountered so far
            res[0] = max(res[0], left + right)
            # Return the depth of the current node
            return max(right, left) + 1
        # Initialize a list to hold the maximum diameter encountered
        res = [0]
        # Call the diameter function starting from the root
        diameter(root, res)
        # Return the maximum diameter encountered
        return res[0]