def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)
