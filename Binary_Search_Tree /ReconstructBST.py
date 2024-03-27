class BST:
    def __init__(self, value, left=None, right=None)    :
        self.value = value
        self.left = left
        self.right = right 


def reconstructBst(preOrderTraversalValue):
    root = BST(preOrderTraversalValue[0])
    left_value = []
    right_value = []
    for n in preOrderTraversalValue[1:]:
        if n < root.value:
            left_value.append(n)
        else:
            right_value.append(n)
        
    if left_value:
        root.left = reconstructBst(left_value)
    if right_value:
        root.right = reconstructBst(right_value)
    return root

lst = [10, 4, 2, 1, 5, 17, 19, 18]
print(reconstructBst(lst))