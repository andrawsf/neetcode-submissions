# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        rootCopy = root
        if root:
            nextToInvert = []
            nextToInvert.append(root)
        else:
            return None

        while nextToInvert:
            next = nextToInvert.pop(0)
            if next.left and next.right:
                #print(f"Swappin {next.left.val} and {next.right.val}")
                nextToInvert.append(next.left)
                nextToInvert.append(next.right)
                left = next.left
                next.left = next.right
                next.right = left
            elif next.left:
                #print(f"Swappin {next.left.val} and {None}")
                nextToInvert.append(next.left)
                next.right = next.left
                next.left = None
            elif next.right:
                #print(f"Swappin {None} and {next.right.val}")
                nextToInvert.append(next.right)
                next.left = next.right
                next.right = None

        return rootCopy



