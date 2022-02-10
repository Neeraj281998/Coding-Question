#Method 1

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        second=slow
        while slow:
            slow.next,prev,slow=prev,slow,slow.next
        while prev:
            if prev.val!=head.val:
                return False
            head=head.next
            prev=prev.next
        return True
      
#Method2

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        rev=None
        while fast and fast.next:
            fast=fast.next.next
            rev,slow.next,slow=slow,rev,slow.next # reverse the while moving fast moving
        if fast:
            slow=slow.next                        #if Fast :slow.next
        while rev and rev.val==slow.val:
            rev=rev.next              
            slow=slow.next
        return not rev
