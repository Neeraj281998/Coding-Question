#Method 1 
# In One Go

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None and headN is None:
            return None
        a=headA
        b=headB
        while (a!=b):
            if a is not None:
                a=a.next
            else:
                a=headB
            if b is not None:
                b=b.next
            else:
                b=headA
        return a
      
#Method 2
    def getIntersectionNode(self, headA, headB):
        # Using Hash Table
        
        temp={}
        while headA is not None:
            if headA not in temp:
                temp[headA]=headA.val
            headA=headA.next
        
        while headB is not None:
            if headB in temp:
                 return headB
            headB=headB.next
        return None
