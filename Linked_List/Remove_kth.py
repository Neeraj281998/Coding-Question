#Keeping dif of n+1 between slow and fast soo that slow will stop before kth element

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(None,head)
        slow=dummy
        fast=dummy
        for i in range(1,n+2):
            fast=fast.next
        while fast!=None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
