# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        deque = collections.deque()
        deque.append(root)

        while deque:
            right = None
            qlen = len(deque)
            for i in range(qlen):
                node = deque.popleft()
                if node:
                    right = node
                    deque.append(node.left)
                    deque.append(node.right)
            if right:
                result.append(right.val)
        return result
        
        