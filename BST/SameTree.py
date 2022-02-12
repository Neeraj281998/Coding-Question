#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

def isSameTree(tree1,tree2) -> bool:
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2 or p.val!=tree2.val:
            return False
        return (self.isSameTree(tree1.left,tree2.left) and self.isSameTree(tree1.right,tree2.right))
        
