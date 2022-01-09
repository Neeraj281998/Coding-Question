class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        dummy=ListNode(0,head)
        cur=dummy
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                
                cur.next=head.next
            else:
                cur=cur.next
            head=head.next
        return dummy.next
            