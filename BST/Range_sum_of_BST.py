    
  #METHOD 1 : easy to understand
def rangeSumBST(self, root: Optional[TreeNode], l: int, h: int) -> int:
        if not root :
            return 
        arr=[]
        def inorder(root,l,h):
            if root.left:
                inorder(root.left,l,h)
            if root.val>=l and root.val<=h:
                arr.append(root.val)
            if root.right:
                inorder(root.right,l,h)
        inorder(root,l,h)
        return sum(arr)
      
 #Method 2:


    def rangeSumBST(self, root: Optional[TreeNode], l: int, h: int,count=0) -> int:
        if not root:
            return 0
        return (root.val if root.val>=l and root.val<=h else 0)+self.rangeSumBST(root.left,l,h)+self.rangeSumBST(root.right,l,h)
