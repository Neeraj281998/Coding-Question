  #Given the root of a binary tree, invert the tree, and return its root.  
  
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left,root.right=root.right,root.left
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            return root
