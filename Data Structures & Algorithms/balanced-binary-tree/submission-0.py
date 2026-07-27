# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        height = {None: 0}
        balance = True

        while(stack):
            node = stack[-1]

            if node.left and node.left not in height:
                stack.append(node.left)
            elif node.right and node.right not in height:
                stack.append(node.right)
            else:
                node = stack.pop()
                left_h = height[node.left]
                right_h = height[node.right]
        
                if abs(left_h - right_h) > 1:
                    return False

                height[node] = 1 + max(left_h, right_h)

        return True



        