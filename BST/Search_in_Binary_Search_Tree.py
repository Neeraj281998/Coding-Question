#Find the node in the BST that the node's value equals val and return the subtree rooted with that node.

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if val<root.val:
                if root.val==val:
                    return root
                if root is None:
                    return 
                return self.searchBST(root.left,val)
            else:
                if root.val==val:
                    return root
                if root is None:
                    return 
                return self.searchBST(root.right,val)
        else:
            return
