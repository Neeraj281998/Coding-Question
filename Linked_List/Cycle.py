#Method 1
#Using memory
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return 
        memo=[]
        while head:
            if not head in memo:
                memo.append(head)
            else:
                return True 
            head=head.next
        return False
      
 #Method 2
# manipulating Data in the Linked List
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head is not None:
            if head.val=="exist":
                return True
            head.val="exist"
            head=head.next
        return False
 
#Method 3

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if (fast==slow):
                break
        if fast==None or fast.next==None:
            return False
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow==fast
                
