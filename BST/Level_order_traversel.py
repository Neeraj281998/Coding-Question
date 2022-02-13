#Method 1 (recursion):

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level=1
        while self.printLevelOrder(root,level):
            level+=1
    def printLevelOrder(self,root,level,temp=[]):
        if not root:
            return False
        if level==1:
            temp.append(root.val)
            return True
        left=self.printLevelOrder(root.left,level-1)
        right=self.printLevelOrder(root.right,level-1)
        
        return left or right
  
  #METHOD 2 :
  #Given the root of a binary tree, return the level order traversal of its nodes' values
  #LeetCode
   def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        result=[]
        queue=[]
        queue.append(root)
        while len(queue)>0:
            ans=[]
            length=len(queue)
            for i in range(length):
                cur=queue.pop(0)
                ans.append(cur.val)
                if cur.left!=None:
                    queue.append(cur.left)
                if cur.right!=None:
                    queue.append(cur.right)
            result.append(ans)
        return result
  
  
